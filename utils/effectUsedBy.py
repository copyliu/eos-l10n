#!/usr/bin/env python3
#======================================================================
# Copyright (C) 2010 Anton Vorobyov
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with eos.  If not, see <http://www.gnu.org/licenses/>.
#======================================================================
"""
Go through all effects and fill them with 'used by' comments.

There're several big stages:
Stage 1. Gather all required data into 'global' dictionaries. We have
2 dictionaries per grouping type, one which lists groups per typeid,
and another which lists typeIDs per group.
Stage 2. Cycle through each effect.
Stage 2.1. Compose similar set of dictionaries like in stage 1, but
this time we take into consideration typeIDs affected by effect picked
in stage 2.
Stage 2.2. Create several lists (1 per grouping type) which will keep
IDs of these groups which will describe set of the typeIDs, and start
iterating. Each iteration one ID will be appended to any of the lists.
Stage 2.2.1. Compose score dictionaries per grouping type, and
calculate total score for given grouping type.
Stage 2.2.2. Pick grouping type with highest score, find winner group
inside grouping type, append its ID to corresponding list created in
stage 2.2. If score is less than certain value, stop iterating. If some
items are not covered by set of winners from lists, they'll be
presented as single items.
Stage 2.3. Print results to file if anything has been changed.

Grouping types used are:
Groups (groupID of an item);
Categories (categoryID of groupID of an item);
Base types (variations, like they appear on eve's variation tab);
Market groups + variations (marketGroupID of an item, plus variations
of all items from given market group, excluding items with
marketGroupID).
Type names (various combinations of words taken from typeName of item).
"""

import copy
import itertools
import math
import os.path
import re
import sqlite3
from optparse import OptionParser

usage = "usage: %prog --database=DB [--debug=DEBUG]"
parser = OptionParser(usage=usage)
parser.add_option("-d", "--database", help="path to eve cache data dump in \
                  sqlite format, default eos database path is used if none \
                  specified",type="string",
                  default=os.path.join("~", ".pyfa","eve.db"))
parser.add_option("-u", "--debug", help="debug level, 0 by default",
                  type="int", default=0)
(options, args) = parser.parse_args()

# Show debugging prints?
# 0 - Don't show debugging stuff and perform actual run
# 1 - Show only for first iteration
# 2 - Show for all iterations
DEBUG_LEVEL = options.debug

# Ways to control process:
# Adjust grouping type weights (more number - better chance to pick
# this grouping type)
GROUP_WEIGHT = 1.0
CATEGORY_WEIGHT = 1.0
BASETYPE_WEIGHT = 1.0
MARKETGROUPWITHVARS_WEIGHT = 0.3
TYPENAMECOMBINATIONS_WEIGHT = 1.0
# If score drops below this value, remaining items will be listed
# without any grouping
LOWEST_SCORE = 0.7
# Adjust scoring formulae
def calc_innerscore(affected_decribed, affected_undescribed, total,
                    pereffect_totalaffected, weight=1.0):
    """Inner score calculation formula"""
    # Percentage of items affected by effect out of total number of
    # items in this group
    coverage_total = (affected_decribed + affected_undescribed) / total
    # Same, but only described/undescribed items are taken
    coverage_described = affected_decribed / total
    coverage_undescribed = affected_undescribed / total
    # Already described items should have less weight
    coverage_additionalfactor = coverage_undescribed + coverage_described * 0
    # If group has just one item - it should have zero score
    affected_total_factor = affected_decribed + affected_undescribed - 1
    innerscore = (coverage_total ** 0.23) * coverage_additionalfactor * \
    affected_total_factor * weight
    return innerscore
def calc_outerscore(innerscore_dict, pereffect_totalaffected, weight):
    """Outer score calculation formula"""
    # Return just max of the inner scores, including weight factor
    if float(len(innerscore_dict)):
        outerscore = innerscore_dict[max(innerscore_dict, key=lambda a:
        innerscore_dict.get(a))] * weight
        return outerscore
    else: return 0.0

# Connect to database and set up cursor
db = sqlite3.connect(os.path.expanduser(options.database))
cursor = db.cursor()

# As we don't rely on eos's overrides, we need to set them manually
OVERRIDES = '''
UPDATE invtypes SET published = '1' WHERE typeName = 'Freki';
UPDATE invtypes SET published = '1' WHERE typeName = 'Mimir';
UPDATE invtypes SET published = '1' WHERE typeName = 'Utu';
UPDATE invtypes SET published = '1' WHERE typeName = 'Adrestia';
'''
for statement in OVERRIDES.split(";\n"):
    cursor.execute(statement)

# Queries to get raw data
QUERY_ALLEFFECTS = 'SELECT effectID, effectName FROM dgmeffects'
# Limit categories to Celestials (2, only for wormhole effects),
# Ships (6), Modules (7), Charges (8), Skills (16), Drones (18),
# Implants (20), Subsystems (32)
QUERY_PUBLISHEDTYPEIDS = 'SELECT it.typeID FROM invtypes AS it INNER JOIN \
invgroups AS ig ON it.groupID = ig.groupID INNER JOIN invcategories AS ic ON \
ig.categoryID = ic.categoryID WHERE it.published = 1 AND \
(ic.categoryID = 2 OR ic.categoryID = 6 OR ic.categoryID = 7 OR \
ic.categoryID = 8 OR ic.categoryID = 16 OR ic.categoryID = 18 OR \
ic.categoryID = 20 OR ic.categoryID = 32)'
QUERY_TYPEID_GROUPID = 'SELECT groupID FROM invtypes WHERE typeID = ? LIMIT 1'
QUERY_GROUPID_CATEGORYID = 'SELECT categoryID FROM invgroups WHERE \
groupID = ? LIMIT 1'
QUERY_TYPEID_PARENTTYPEID = 'SELECT parentTypeID FROM invmetatypes WHERE \
typeID = ? LIMIT 1'
QUERY_TYPEID_MARKETGROUPID = 'SELECT marketGroupID FROM invtypes WHERE \
typeID = ? LIMIT 1'
QUERY_TYPEID_TYPENAME = 'SELECT typeName FROM invtypes WHERE typeID = ? \
LIMIT 1'
QUERY_MARKETGROUPID_PARENTGROUPID = 'SELECT parentGroupID FROM \
invmarketgroups WHERE marketGroupID = ? LIMIT 1'
QUERY_EFFECTID_TYPEID = 'SELECT typeID FROM dgmtypeeffects WHERE effectID = ?'
# Queries for printing
QUERY_GROUPID_GROUPNAME = 'SELECT groupName FROM invgroups WHERE groupID = ? \
LIMIT 1'
QUERY_CATEGORYID_CATEGORYNAME = 'SELECT categoryName FROM invcategories \
WHERE categoryID = ? LIMIT 1'
QUERY_MARKETGROUPID_MARKETGROUPNAME = 'SELECT marketGroupName FROM \
invmarketgroups WHERE marketGroupID = ? LIMIT 1'

# Compose list of effects w/o symbols which eos doesn't take into
# consideration, we'll use it to find proper effect IDs from file
# names
globalmap_effectnameeos_effectid = {}
STRIPSPEC = "[^A-Za-z0-9]"
cursor.execute(QUERY_ALLEFFECTS)
for row in cursor:
    effectid = row[0]
    effectnamedb = row[1]
    effectnameeos = re.sub(STRIPSPEC, "", effectnamedb)
    globalmap_effectnameeos_effectid[effectnameeos] = effectid

# Stage 1

# Published types set
publishedtypes = set()
cursor.execute(QUERY_PUBLISHEDTYPEIDS)
for row in cursor:
    publishedtypes.add(row[0])

# Compose group maps
# { groupid : set(typeid) }
globalmap_groupid_typeid = {}
# { typeid : groupid }
globalmap_typeid_groupid = {}
for typeid in publishedtypes:
    groupid = 0
    cursor.execute(QUERY_TYPEID_GROUPID, (typeid,))
    for row in cursor:
        groupid = row[0]
    if not groupid in globalmap_groupid_typeid:
        globalmap_groupid_typeid[groupid] = set()
    globalmap_groupid_typeid[groupid].add(typeid)
    globalmap_typeid_groupid[typeid] = groupid

# Category maps
# { categoryid : set(typeid) }
globalmap_categoryid_typeid =  {}
# { typeid : categoryid }
globalmap_typeid_categoryid =  {}
for typeid in publishedtypes:
    categoryid = 0
    cursor.execute(QUERY_GROUPID_CATEGORYID,
                   (globalmap_typeid_groupid[typeid],))
    for row in cursor:
        categoryid = row[0]
    if not categoryid in globalmap_categoryid_typeid:
        globalmap_categoryid_typeid[categoryid] = set()
    globalmap_categoryid_typeid[categoryid].add(typeid)
    globalmap_typeid_categoryid[typeid] = categoryid

# Base type maps
# { basetypeid : set(typeid) }
globalmap_basetypeid_typeid =  {}
# { typeid : basetypeid }
globalmap_typeid_basetypeid =  {}
for typeid in publishedtypes:
    # Not all typeIDs in the database have baseTypeID, so assign some
    # default value to it
    basetypeid = 0
    cursor.execute(QUERY_TYPEID_PARENTTYPEID, (typeid,))
    for row in cursor:
        basetypeid = row[0]
    # If base type is not published or is not set in database, consider
    # item as variation of self
    if basetypeid not in publishedtypes:
        basetypeid = typeid
    if not basetypeid in globalmap_basetypeid_typeid:
        globalmap_basetypeid_typeid[basetypeid] = set()
    globalmap_basetypeid_typeid[basetypeid].add(typeid)
    globalmap_typeid_basetypeid[typeid] = basetypeid

# Market group maps - we won't use these for further processing, but
# just as helper for composing other maps
# { marketgroupid : set(typeid) }
globalmap_marketgroupid_typeid =  {}
# { typeid : set(marketgroupid) }
globalmap_typeid_marketgroupid =  {}
for typeid in publishedtypes:
    marketgroupid = 0
    cursor.execute(QUERY_TYPEID_MARKETGROUPID, (typeid,))
    for row in cursor:
        marketgroupid = row[0]
    if not marketgroupid:
        continue
    if not marketgroupid in globalmap_marketgroupid_typeid:
        globalmap_marketgroupid_typeid[marketgroupid] = set()
    globalmap_marketgroupid_typeid[marketgroupid].add(typeid)
# Copy items to all parent market groups
INITIALMARKETGROUPIDS = tuple(globalmap_marketgroupid_typeid)
for marketgroupid in INITIALMARKETGROUPIDS:
    # Limit depths for case if database will refer to groups making
    # the loop
    cyclingmarketgroupid = marketgroupid
    for depth in range(20):
        cursor_parentmarket = db.cursor()
        cursor_parentmarket.execute(QUERY_MARKETGROUPID_PARENTGROUPID,
                                    (cyclingmarketgroupid,))
        for row in cursor_parentmarket:
            cyclingmarketgroupid = row[0]
        if cyclingmarketgroupid:
            if not cyclingmarketgroupid in globalmap_marketgroupid_typeid:
                globalmap_marketgroupid_typeid[cyclingmarketgroupid] = set()
            globalmap_marketgroupid_typeid[cyclingmarketgroupid].update\
            (globalmap_marketgroupid_typeid[marketgroupid])
        else: break
# Now, make a reverse map
for marketgroupid, typeidset in globalmap_marketgroupid_typeid.items():
    for typeid in typeidset:
        if not typeid in globalmap_typeid_marketgroupid:
            globalmap_typeid_marketgroupid[typeid] = set()
        globalmap_typeid_marketgroupid[typeid].add(marketgroupid)

# Combine market groups and variations
# { marketgroupid : set(typeidwithvariations) }
globalmap_marketgroupid_typeidwithvariations = \
copy.deepcopy(globalmap_marketgroupid_typeid)
# { typeidwithvariations : set(marketgroupid) }
globalmap_typeidwithvariations_marketgroupid = {}
for marketgroupid in globalmap_marketgroupid_typeidwithvariations:
    typestoadd = set()
    for typeid in globalmap_marketgroupid_typeidwithvariations[marketgroupid]:
        if typeid in globalmap_basetypeid_typeid:
            for variationid in globalmap_basetypeid_typeid[typeid]:
                # Do not include items which have market group, even if
                # they're variation
                if variationid in globalmap_typeid_marketgroupid:
                    typestoadd.add(variationid)
    globalmap_marketgroupid_typeidwithvariations[marketgroupid].update\
    (typestoadd)
# Make reverse map using simple way too
for marketgroupid, typeidwithvariationsset in \
globalmap_marketgroupid_typeidwithvariations.items():
    for typeid in typeidwithvariationsset:
        if not typeid in globalmap_typeidwithvariations_marketgroupid:
            globalmap_typeidwithvariations_marketgroupid[typeid] = set()
        globalmap_typeidwithvariations_marketgroupid[typeid].add(marketgroupid)

# Item names map
# We need to include category ID to avoid combining items from different
# categories (e.g. skills and modules) and length of original name to
# assess word coverage of various type name combinations
# { ((typenamecombination), categoryid) : set(typeid) }
globalmap_typenamecombinationtuple_typeid =  {}
# { typeid : (set((typenamecombination)), len(typename)) }
globalmap_typeid_typenamecombinationtuple =  {}
for typeid in publishedtypes:
    typename = ""
    cursor.execute(QUERY_TYPEID_TYPENAME, (typeid,))
    for row in cursor:
        typename = row[0]
    # Split strings into separate words
    typenamesplitted = []
    # Start from the whole type name
    remainingstring = typename
    # We will pick word each iteration
    iterate = True
    while iterate:
        # This regexp helps to split into words with spaces and dashes
        # between them, for example: CX|-|1, Hardwiring| - |Inherent,
        # Zainou| |'Snapshot'
        separatingpattern_general = \
        "((?P<left_part>[^ -]+)(?P<separator>[ -]+)(?P<right_part>([^ -].*)))"
        # This will help to split names like those used in implants,
        # for example: ZET||500, EE||8
        separatingpattern_series = \
        "((?P<left_part>[A-Za-z]{2,4})(?P<right_part>[0-9]{1,4}.*))"
        # Check remainingstring using both criteria
        matchobject_general = re.match(separatingpattern_general,
                                       remainingstring)
        matchobject_series = re.match(separatingpattern_series,
                                      remainingstring)
        # Now, we need to find which criterion satisfies us
        usegeneral = False
        useseries = False
        # If remaining string meets both criteria
        if matchobject_general and matchobject_series:
            # We check which occurs first and pick it
            if len(matchobject_general.group("left_part")) <= \
            len(matchobject_series.group("left_part")):
                usegeneral = True
            else:
                useseries = True
        # If only one criterion is met, just pick it
        elif matchobject_general:
            usegeneral = True
        elif matchobject_series:
            useseries = True
        # Now, actually split string into word, separator and remaining
        # string and append word to list of words of current typename
        if usegeneral:
            newword = matchobject_general.group("left_part")
            separator = matchobject_general.group("separator")
            remainingstring = matchobject_general.group("right_part")
            typenamesplitted.append(newword)
        elif useseries:
            newword = matchobject_series.group("left_part")
            separator = ""
            remainingstring = matchobject_series.group("right_part")
            typenamesplitted.append(newword)
        # If we didn't match any regexp, then we see last word - append
        # it too and stop iterating
        else:
            typenamesplitted.append(remainingstring)
            iterate = False
    # Iterate through number of words which will be used to compose
    # combinations
    for wordnumindex in range(len(typenamesplitted)):
        # Iterate through all possible combinations
        for typenamecombination in itertools.combinations(typenamesplitted,
                                                          wordnumindex + 1):
            typenamecombinationtuple = (typenamecombination,
                                        globalmap_typeid_categoryid[typeid])
            if not typenamecombinationtuple in \
            globalmap_typenamecombinationtuple_typeid:
                globalmap_typenamecombinationtuple_typeid\
                [typenamecombinationtuple] = set()
            globalmap_typenamecombinationtuple_typeid\
            [typenamecombinationtuple].add(typeid)
            if not typeid in globalmap_typeid_typenamecombinationtuple:
                globalmap_typeid_typenamecombinationtuple[typeid] = \
                (set(), len(typenamesplitted))
            globalmap_typeid_typenamecombinationtuple[typeid][0].add\
            (typenamecombination)

# Stage 2

#Go through effect files one-by-one
effectsPath = os.path.join("..", "effects")
for effectFileName in os.listdir(effectsPath):
    basename, extension = effectFileName.split('.')
    #Ignore non-py files and exclude implementation-specific 'effects'
    if extension == "py" and not basename in ("__init__"):
        ######################## Stage 2.1 ########################
        #Data regarding which items are affected by current effect
        perEffectList_usedByTypes = set()
        cursor.execute(QUERY_EFFECTID_TYPEID, (globalmap_effectnameeos_effectid[basename],))
        for rowTypes in cursor:
            typeid = rowTypes[0]
            if typeid in publishedtypes: perEffectList_usedByTypes.add(typeid)
        #Number of items affected by current effect
        pereffect_totalaffected = len(perEffectList_usedByTypes)

        #Compose per-group map of items which are affected by current effect
        # { groupID : (set(typeid), describes) }
        perEffectMap_groupID_typeID = {}
        for typeid in perEffectList_usedByTypes:
            groupID = globalmap_typeid_groupid[typeid]
            if not groupID in perEffectMap_groupID_typeID: perEffectMap_groupID_typeID[groupID] = [set(), False]
            perEffectMap_groupID_typeID[groupID][0].add(typeid)

        #Now, per-category map of items
        # { categoryid : (set(typeid), describes) }
        perEffectMap_categoryID_typeID = {}
        for typeid in perEffectList_usedByTypes:
            categoryid = globalmap_typeid_categoryid[typeid]
            if not categoryid in perEffectMap_categoryID_typeID: perEffectMap_categoryID_typeID[categoryid] = [set(), False]
            perEffectMap_categoryID_typeID[categoryid][0].add(typeid)

        #Per-baseType map of variations
        # { basetypeid : (set(typeid), describes) }
        perEffectMap_baseTypeID_typeID = {}
        for typeid in perEffectList_usedByTypes:
            basetypeid = globalmap_typeid_basetypeid[typeid]
            if not basetypeid in perEffectMap_baseTypeID_typeID: perEffectMap_baseTypeID_typeID[basetypeid] = [set(), False]
            perEffectMap_baseTypeID_typeID[basetypeid][0].add(typeid)

        #Per-marketGroup map with variations
        # { marketgroupid : (set(typeidwithvariations), describes) }
        perEffectMap_marketGroupID_typeIDWithVariations = {}
        for typeid in perEffectList_usedByTypes:
            if typeid in globalmap_typeid_marketgroupid: marketGroupIDs = globalmap_typeid_marketgroupid[typeid]
            else: marketGroupIDs = set()
            for marketgroupid in marketGroupIDs:
                if not marketgroupid in perEffectMap_marketGroupID_typeIDWithVariations: perEffectMap_marketGroupID_typeIDWithVariations[marketgroupid] = [set(), False]
                perEffectMap_marketGroupID_typeIDWithVariations[marketgroupid][0].add(typeid)

        #Per-typenamecombination map
        # { ((typenamecombination), categoryid) : (set(typeid), describes) }
        perEffectMap_typeNameCombinationTuple_typeID = {}
        for typeid in perEffectList_usedByTypes:
            typeNameCombinations = globalmap_typeid_typenamecombinationtuple[typeid][0]
            for typenamecombination in typeNameCombinations:
                typenamecombinationtuple = (typenamecombination, globalmap_typeid_categoryid[typeid])
                if not typenamecombinationtuple in perEffectMap_typeNameCombinationTuple_typeID: perEffectMap_typeNameCombinationTuple_typeID[typenamecombinationtuple] = [set(), False]
                perEffectMap_typeNameCombinationTuple_typeID[typenamecombinationtuple][0].add(typeid)

        stopDebugPrints = False
        if DEBUG_LEVEL >= 1:
            print("\nEffect:", basename)
            print("Total items affected: {0}".format(pereffect_totalaffected))

        ######################## Stage 2.2 ########################
        #This set holds all IDs of already described items
        perEffect_describedTypes = set()
        #These lists contain IDs of each grouping type which are used
        #to describe items from the set above
        describedByGroup = []
        describedByCategory = []
        describedByBaseType = []
        describedByMarketGroupWithVars = []
        describedByTypeNameCombination = []

        #Each iteration some group is picked which
        #will be used to describe set of items
        iterate = True
        while iterate:
            ####################### Stage 2.2.1 #######################
            #stores scores for each group which describe set of items
            groupScore = {}
            #define weight of this grouping type
            for groupID in perEffectMap_groupID_typeID:
                #skip groups which are already used for item description
                #(have 'describes' flag set to True)
                if not perEffectMap_groupID_typeID[groupID][1]:
                    #Now we should calculate score for current groupID which has items affected by current effect
                    #Items from current group affected by current effect
                    affectedItemsFromCurrentGroup = perEffectMap_groupID_typeID[groupID][0]
                    #Number of affected items from current group; already described
                    affected_decribed = len(affectedItemsFromCurrentGroup.intersection(perEffect_describedTypes))
                    #yet undescribed
                    affected_undescribed =  len(affectedItemsFromCurrentGroup.difference(perEffect_describedTypes))
                    #total number of items from this group (not necessarily affected by current effect)
                    total = len(globalmap_groupid_typeid[groupID])
                    #calculate inner score and push it into score dictionary for current grouping type
                    groupScore[groupID] = calc_innerscore(affected_decribed, affected_undescribed, total, pereffect_totalaffected)
                    #Debug prints for inner data
                    if DEBUG_LEVEL >= 1 and not stopDebugPrints:
                        cursor.execute(QUERY_GROUPID_GROUPNAME, (groupID,))
                        for row in cursor: groupName = row[0]
                        coverage = (affected_decribed + affected_undescribed)/total * 100
                        #If debug level is 1, we print results only for 1st iteration
                        if DEBUG_LEVEL == 1: print("Group: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(groupName, affected_undescribed, total, coverage, groupScore[groupID]))
                        #If it's 2, we print results for each iteration, so we need to
                        #include number of already described items
                        if DEBUG_LEVEL == 2: print("Group: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(groupName, affected_undescribed, affected_decribed, total, coverage, groupScore[groupID]))
            #Calculate outer score for this grouping type
            groupOuterScore = calc_outerscore(groupScore, pereffect_totalaffected, GROUP_WEIGHT)
            #Debug print for outer data
            if DEBUG_LEVEL >= 1 and not stopDebugPrints: print("Groups outer score: {0:.3}".format(groupOuterScore))

            categoryScore = {}
            for categoryid in perEffectMap_categoryID_typeID:
                if not perEffectMap_categoryID_typeID[categoryid][1]:
                    affectedItemsFromCurrentCategory = perEffectMap_categoryID_typeID[categoryid][0]
                    affected_decribed = len(affectedItemsFromCurrentCategory.intersection(perEffect_describedTypes))
                    affected_undescribed =  len(affectedItemsFromCurrentCategory.difference(perEffect_describedTypes))
                    total = len(globalmap_categoryid_typeid[categoryid])
                    categoryScore[categoryid] = calc_innerscore(affected_decribed, affected_undescribed, total, pereffect_totalaffected)
                    if DEBUG_LEVEL >= 1 and not stopDebugPrints:
                        cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (categoryid,))
                        for row in cursor: categoryName = row[0]
                        coverage = (affected_decribed + affected_undescribed)/total * 100
                        if DEBUG_LEVEL == 1: print("Category: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(categoryName, affected_undescribed, total, coverage, categoryScore[categoryid]))
                        if DEBUG_LEVEL == 2: print("Category: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(categoryName, affected_undescribed, affected_decribed, total, coverage, categoryScore[categoryid]))
            categoryOuterScore = calc_outerscore(categoryScore, pereffect_totalaffected, CATEGORY_WEIGHT)
            if DEBUG_LEVEL >= 1 and not stopDebugPrints: print("Category outer score: {0:.3}".format(categoryOuterScore))

            baseTypeScore = {}
            for basetypeid in perEffectMap_baseTypeID_typeID:
                if not perEffectMap_baseTypeID_typeID[basetypeid][1]:
                    affectedItemsFromCurrentBaseType = perEffectMap_baseTypeID_typeID[basetypeid][0]
                    affected_decribed = len(affectedItemsFromCurrentBaseType.intersection(perEffect_describedTypes))
                    affected_undescribed =  len(affectedItemsFromCurrentBaseType.difference(perEffect_describedTypes))
                    total = len(globalmap_basetypeid_typeid[basetypeid])
                    baseTypeScore[basetypeid] = calc_innerscore(affected_decribed, affected_undescribed, total, pereffect_totalaffected)
                    if DEBUG_LEVEL >= 1 and not stopDebugPrints:
                        cursor.execute(QUERY_TYPEID_TYPENAME, (basetypeid,))
                        for row in cursor: baseTypeName = row[0]
                        coverage = (affected_decribed + affected_undescribed)/total * 100
                        if DEBUG_LEVEL == 1: print("Base item: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(baseTypeName, affected_undescribed, total, coverage, baseTypeScore[basetypeid]))
                        if DEBUG_LEVEL == 2: print("Base item: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(baseTypeName, affected_undescribed, affected_decribed, total, coverage, baseTypeScore[basetypeid]))
            baseTypeOuterScore = calc_outerscore(baseTypeScore, pereffect_totalaffected, BASETYPE_WEIGHT)
            #Print outer data
            if DEBUG_LEVEL >= 1 and not stopDebugPrints: print("Base item outer score: {0:.3}".format(baseTypeOuterScore))

            marketGroupWithVarsScore = {}
            for marketgroupid in perEffectMap_marketGroupID_typeIDWithVariations:
                if not perEffectMap_marketGroupID_typeIDWithVariations[marketgroupid][1]:
                    affectedItemsFromCurrentMarketGroupWithVars = perEffectMap_marketGroupID_typeIDWithVariations[marketgroupid][0]
                    affected_decribed = len(affectedItemsFromCurrentMarketGroupWithVars.intersection(perEffect_describedTypes))
                    affected_undescribed =  len(affectedItemsFromCurrentMarketGroupWithVars.difference(perEffect_describedTypes))
                    total = len(globalmap_marketgroupid_typeidwithvariations[marketgroupid])
                    marketGroupWithVarsScore[marketgroupid] = calc_innerscore(affected_decribed, affected_undescribed, total, pereffect_totalaffected)
                    if DEBUG_LEVEL >= 1 and not stopDebugPrints:
                        cursor.execute(QUERY_MARKETGROUPID_MARKETGROUPNAME, (marketgroupid,))
                        for row in cursor: marketGroupName = row[0]
                        #Prepend market group name with its parents names
                        prependParentID = marketgroupid
                        #Limit depth in case if market groups form a loop
                        for depth in range(20):
                            cursor_parentmarket = db.cursor()
                            cursor_parentmarket.execute(QUERY_MARKETGROUPID_PARENTGROUPID, (prependParentID,))
                            for row in cursor_parentmarket:
                                prependParentID = row[0]
                            if prependParentID:
                                cursor.execute(QUERY_MARKETGROUPID_MARKETGROUPNAME, (prependParentID,))
                                for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                            else: break
                        coverage = (affected_decribed + affected_undescribed)/total * 100
                        if DEBUG_LEVEL == 1: print("Market group with variations: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(marketGroupName, affected_undescribed, total, coverage, marketGroupWithVarsScore[marketgroupid]))
                        if DEBUG_LEVEL == 2: print("Market group with variations: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(marketGroupName, affected_undescribed, affected_decribed, total, coverage, marketGroupWithVarsScore[marketgroupid]))
            marketGroupWithVarsOuterScore = calc_outerscore(marketGroupWithVarsScore, pereffect_totalaffected, MARKETGROUPWITHVARS_WEIGHT)
            if DEBUG_LEVEL >= 1 and not stopDebugPrints: print("Market group outer score: {0:.3}".format(marketGroupWithVarsOuterScore))

            typeNameCombinationScore = {}
            for typenamecombinationtuple in perEffectMap_typeNameCombinationTuple_typeID:
                if not perEffectMap_typeNameCombinationTuple_typeID[typenamecombinationtuple][1]:
                    affectedItemsFromCurrenttypeNameCombination = perEffectMap_typeNameCombinationTuple_typeID[typenamecombinationtuple][0]
                    affected_decribed = len(affectedItemsFromCurrenttypeNameCombination.intersection(perEffect_describedTypes))
                    affected_undescribed =  len(affectedItemsFromCurrenttypeNameCombination.difference(perEffect_describedTypes))
                    total = len(globalmap_typenamecombinationtuple_typeid[typenamecombinationtuple])
                    #Type names are special: wee also need to consider how certain
                    #word combination covers full type name. We start from zero
                    averageCoverage = 0
                    itemsNamedLikeThis = perEffectMap_typeNameCombinationTuple_typeID[typenamecombinationtuple][0]
                    for typeid in itemsNamedLikeThis:
                        #Add number of words in combination divided by total number of words from any given item
                        averageCoverage += len(typenamecombinationtuple[0])/globalmap_typeid_typenamecombinationtuple[typeid][1]
                    #Then divide by number of items we checked, making it real average
                    averageCoverage = averageCoverage/len(itemsNamedLikeThis)
                    #Pass average coverage as additional balancing factor
                    typeNameCombinationScore[typenamecombinationtuple] = calc_innerscore(affected_decribed, affected_undescribed, total, pereffect_totalaffected, 0.2 + averageCoverage*0.8)
                    if DEBUG_LEVEL >= 1 and not stopDebugPrints:
                        typeNameCombinationPrintable = " ".join(typenamecombinationtuple[0])
                        coverage = (affected_decribed + affected_undescribed)/total * 100
                        if DEBUG_LEVEL == 1: print("Type name combination: \"{0}\": {1}/{2} ({3:.3}%, inner score: {4:.3})".format(typeNameCombinationPrintable, affected_undescribed, total, coverage, typeNameCombinationScore[typenamecombinationtuple]))
                        if DEBUG_LEVEL == 2: print("Type name combination: \"{0}\": {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(typeNameCombinationPrintable, affected_undescribed, affected_decribed, total, coverage, typeNameCombinationScore[typenamecombinationtuple]))
            typeNameCombinationOuterScore = calc_outerscore(typeNameCombinationScore, pereffect_totalaffected, TYPENAMECOMBINATIONS_WEIGHT)
            if DEBUG_LEVEL >= 1 and not stopDebugPrints: print("Type name combination outer score: {0:.3}".format(typeNameCombinationOuterScore))

            #Don't print anything after 1st iteration at 1st debugging level
            if DEBUG_LEVEL == 1: stopDebugPrints = True
            #Print separator for 2nd debugging level, to separate debug data of one
            #iteration from another
            if DEBUG_LEVEL >= 2: print("---")

            ####################### Stage 2.2.2 #######################
            #Pick max score from outer scores of all grouping types
            maxOuterScore = max(groupOuterScore, categoryOuterScore, baseTypeOuterScore, marketGroupWithVarsOuterScore, typeNameCombinationOuterScore)
            #define lower limit for score, below which there will be no winners
            if maxOuterScore >= LOWEST_SCORE:
                #If scores are similar, priorities are: category > group > name > marketGroup > baseType
                if maxOuterScore == categoryOuterScore:
                    #pick ID of category which has highest score among other categories
                    categoryWinner = max(categoryScore, key=categoryScore.get)
                    #Add it to the list of categories which describe set of items
                    describedByCategory.append(categoryWinner)
                    #add all items described by winning category into set of described items
                    perEffect_describedTypes |= globalmap_categoryid_typeid[categoryWinner]
                    #set 'describes' flag to avoid processing of this category
                    #during following iterations
                    perEffectMap_categoryID_typeID[categoryWinner][1] = True
                elif maxOuterScore == groupOuterScore:
                    groupWinner = max(groupScore, key=groupScore.get)
                    describedByGroup.append(groupWinner)
                    perEffect_describedTypes |= globalmap_groupid_typeid[groupWinner]
                    perEffectMap_groupID_typeID[groupWinner][1] = True
                elif maxOuterScore == typeNameCombinationOuterScore:
                    typeNameCombinationWinner = max(typeNameCombinationScore, key=typeNameCombinationScore.get)
                    describedByTypeNameCombination.append(typeNameCombinationWinner)
                    perEffect_describedTypes |= globalmap_typenamecombinationtuple_typeid[typeNameCombinationWinner]
                    perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationWinner][1] = True
                elif maxOuterScore == marketGroupWithVarsOuterScore:
                    marketGroupWithVarsWinner = max(marketGroupWithVarsScore, key=marketGroupWithVarsScore.get)
                    describedByMarketGroupWithVars.append(marketGroupWithVarsWinner)
                    perEffect_describedTypes |= globalmap_marketgroupid_typeidwithvariations[marketGroupWithVarsWinner]
                    perEffectMap_marketGroupID_typeIDWithVariations[marketGroupWithVarsWinner][1] = True
                elif maxOuterScore == baseTypeOuterScore:
                    baseTypeWinner = max(baseTypeScore, key=baseTypeScore.get)
                    describedByBaseType.append(baseTypeWinner)
                    perEffect_describedTypes |= globalmap_basetypeid_typeid[baseTypeWinner]
                    perEffectMap_baseTypeID_typeID[baseTypeWinner][1] = True
            #Stop if we have score less than some critical value, all undescribed
            #items will be provided as plain list
            else: iterate = False
            #Also stop if we described all items
            if perEffectList_usedByTypes.issubset(perEffect_describedTypes): iterate = False
        singleItems = set(perEffectList_usedByTypes).difference(perEffect_describedTypes)
        if DEBUG_LEVEL >= 1:
            print("Effect will be described by:")
            print("Single item IDs:", singleItems)
            print("Group IDs:", describedByGroup)
            print("Category IDs:", describedByCategory)
            print("Base item IDs:", describedByBaseType)
            print("Market group with variations IDs:", describedByMarketGroupWithVars)
            print("Type name combinations:", describedByTypeNameCombination)

        ######################## Stage 2.1 ########################
        #Read effects file and split it into lines
        effectFile = open(os.path.join(effectsPath, effectFileName), 'r')
        effectContentsSource = effectFile.read()
        effectFile.close()
        effectLines = effectContentsSource.split("\n")
        #Delete old comments from file contents
        numberOfCommentLines = 0
        for line in effectLines:
            if line:
                if line[0] == "#": numberOfCommentLines += 1
                else: break
            else: break
        for i in range(numberOfCommentLines):
            del effectLines[0]

        #These lists will contain IDs and some metadata in tuples
        printing_types = []
        printing_groups = []
        printing_categories = []
        printing_baseTypes = []
        printing_marketGroupsWithVars = []
        printing_typeNameCombinationTuples = []

        #Gather data for printing in the form of tuples
        #Each tuple has grouping type ID, human-readable name and category name
        for typeid in singleItems:
            typename = ""
            cursor.execute(QUERY_TYPEID_TYPENAME, (typeid,))
            for row in cursor: typename = row[0]
            categoryName = ""
            cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (globalmap_typeid_categoryid[typeid],))
            for row in cursor: categoryName = row[0]
            printing_types.append((typeid, typename, categoryName))
        for groupID in describedByGroup:
            groupName = ""
            cursor.execute(QUERY_GROUPID_GROUPNAME, (groupID,))
            for row in cursor: groupName = row[0]
            categoryid = 0
            cursor.execute(QUERY_GROUPID_CATEGORYID, (groupID,))
            for row in cursor: categoryid = row[0]
            categoryName = ""
            cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (categoryid,))
            for row in cursor: categoryName = row[0]
            printing_groups.append((groupID, groupName, categoryName))
        for categoryid in describedByCategory:
            categoryName = ""
            cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (categoryid,))
            for row in cursor: categoryName = row[0]
            printing_categories.append((categoryid, categoryName))
        for basetypeid in describedByBaseType:
            baseTypeName = ""
            cursor.execute(QUERY_TYPEID_TYPENAME, (basetypeid,))
            for row in cursor: baseTypeName = row[0]
            categoryName = ""
            cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (globalmap_typeid_categoryid[basetypeid],))
            for row in cursor: categoryName = row[0]
            printing_baseTypes.append((basetypeid, baseTypeName, categoryName))
        for marketgroupid in describedByMarketGroupWithVars:
            cursor.execute(QUERY_MARKETGROUPID_MARKETGROUPNAME, (marketgroupid,))
            for row in cursor: marketGroupName = row[0]
            #Prepend market group name with its parents names
            prependParentID = marketgroupid
            #Limit depth to avoid looping, as usual
            for depth in range(20):
                cursor_parentmarket = db.cursor()
                cursor_parentmarket.execute(QUERY_MARKETGROUPID_PARENTGROUPID, (prependParentID,))
                for row in cursor_parentmarket:
                    prependParentID = row[0]
                if prependParentID:
                    cursor.execute(QUERY_MARKETGROUPID_MARKETGROUPNAME, (prependParentID,))
                    for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                else: break
            printing_marketGroupsWithVars.append((marketgroupid, marketGroupName))
        for typenamecombinationtuple in describedByTypeNameCombination:
            typeNameCombinationPrint = " ".join(typenamecombinationtuple[0])
            categoryName = ""
            cursor.execute(QUERY_CATEGORYID_CATEGORYNAME, (typenamecombinationtuple[1],))
            for row in cursor: categoryName = row[0]
            printing_typeNameCombinationTuples.append((typenamecombinationtuple, typeNameCombinationPrint, categoryName))

        #Use separate list per grouping type to easy grouping type sorting
        printing_typeLines = []
        #Sort by item name first
        printing_types = sorted(printing_types, key=lambda tuple: tuple[1])
        #Then sort by category name
        printing_types = sorted(printing_types, key=lambda tuple: tuple[2])
        for type in printing_types:
            #Append line for printing to list
            printing_typeLines.append("#{0}: {1}".format(type[2], type[1]))
        printing_groupLines = []
        printing_groups = sorted(printing_groups, key=lambda tuple: tuple[1])
        printing_groups = sorted(printing_groups, key=lambda tuple: tuple[2])
        for group in printing_groups:
            printing_groupLines.append("#{0}s from group: {1} ({2} of {3})".format(group[2], group[1], len(perEffectMap_groupID_typeID[group[0]][0]), len(globalmap_groupid_typeid[group[0]])))
        printing_categoryLines = []
        printing_categories = sorted(printing_categories, key=lambda tuple: tuple[1])
        for category in printing_categories:
            printing_categoryLines.append("#Items from category: {0} ({1} of {2})".format(category[1], len(perEffectMap_categoryID_typeID[category[0]][0]), len(globalmap_categoryid_typeid[category[0]])))
        printing_baseTypeLines = []
        printing_baseTypes = sorted(printing_baseTypes, key=lambda tuple: tuple[1])
        printing_baseTypes = sorted(printing_baseTypes, key=lambda tuple: tuple[2])
        for baseType in printing_baseTypes:
            printing_baseTypeLines.append("#Variations of {0}: {1} ({2} of {3})".format(baseType[2].lower(), baseType[1], len(perEffectMap_baseTypeID_typeID[baseType[0]][0]), len(globalmap_basetypeid_typeid[baseType[0]])))
        printing_marketGroupWithVarsLines = []
        printing_marketGroupsWithVars = sorted(printing_marketGroupsWithVars, key=lambda tuple: tuple[1])
        for marketGroup in printing_marketGroupsWithVars:
            printing_marketGroupWithVarsLines.append("#Items from market group: {0} ({1} of {2})".format(marketGroup[1], len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroup[0]][0]), len(globalmap_marketgroupid_typeidwithvariations[marketGroup[0]])))
        printing_typeNameCombinationTupleLines = []
        printing_typeNameCombinationTuples = sorted(printing_typeNameCombinationTuples, key=lambda tuple: tuple[1])
        printing_typeNameCombinationTuples = sorted(printing_typeNameCombinationTuples, key=lambda tuple: tuple[2])
        for typenamecombination in printing_typeNameCombinationTuples:
            printing_typeNameCombinationTupleLines.append("#{0}s named like: {1} ({2} of {3})".format(typenamecombination[2], typenamecombination[1], len(perEffectMap_typeNameCombinationTuple_typeID[typenamecombination[0]][0]), len(globalmap_typenamecombinationtuple_typeid[typenamecombination[0]])))

        #Compose single list of lines using custom sorting
        commentLines = printing_categoryLines + printing_groupLines + printing_typeNameCombinationTupleLines + printing_marketGroupWithVarsLines + printing_baseTypeLines + printing_typeLines
        #Prepend everything with used by
        if commentLines: commentLines = ["#Used by:"] + commentLines
        #If effect isn't used, write it to file and to terminal
        else:
            commentLines = ["#Not used by any item"]
            print("Warning: effect file " + basename + " is not used by any item")
        #Combine "used by" comment lines and actual effect lines
        outputLines = commentLines + effectLines
        #Combine all lines into single string
        effectContentsProcessed = "\n".join(outputLines)
        #If we're not debugging and contents actually changed - write changes to the file
        if DEBUG_LEVEL == 0 and (effectContentsProcessed != effectContentsSource):
            effectFile = open(os.path.join(effectsPath, effectFileName), 'w')
            effectFile.write(effectContentsProcessed)
            effectFile.close()
        elif DEBUG_LEVEL >= 2:
            print("Comment to write to file:")
            print("\n".join(commentLines))
