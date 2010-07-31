#!/usr/bin/env python3
#Copyright 2010 Anton Vorobyov
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
This script goes through all implemented effects and fills them with comments by which items effect is used
'''
#A bit of explanation. There're several big stages:
#Stage 1. Gather all required data into 'global' dictionaries. We have
#2 dictionaries per grouping type, one which lists groups per typeID,
#and another which lists typeIDs per group.
#Stage 2. Cycle through each effect.
#Stage 2.1. Compose similar set of dictionaries like in stage 1, but this time
#we take into consideration typeIDs affected by effect picked in stage 2.
#Stage 2.2. Create several lists (1 per grouping type) which will keep IDs of
#these groups which will describe set of the typeIDs, and start iterating.
#Each iteration one ID will be appended to any of the lists.
#Stage 2.2.1. Compose score dictionaries per grouping type, and calculate total
#score for given grouping type
#Stage 2.2.2. Pick grouping type with highest score, find winner group inside
#grouping type, append its ID to corresponding list created in stage 2.2. If
#score is less than certain value, stop iterating. If some items are not covered
#by set of winners from lists, they'll be presented as single items.
#Stage 2.3. Print results to file if anything has been changed
#
#Grouping types used are:
#Groups (groupID of an item)
#Categories (categoryID of groupID of an item)
#BaseTypes (variations, like they appear on eve's variation tab)
#Market groups + variations (market groups like usual, plus variations
#of all items from it)

import sys
sys.path.append("..")

from optparse import OptionParser
import sqlite3
import os.path
import re
import math
import itertools
import copy

usage = "usage: %prog --database=DB [--debug=DEBUG]"
parser = OptionParser(usage=usage)
parser.add_option("-d", "--database", help="path to eve cache data dump in sqlite format, default pyfa database path is used if none specified", type="string", default=os.path.join("~", ".pyfa","eve.db"))
parser.add_option("-u", "--debug", help="debug level, 0 by default", type="int", default=0)
(options, args) = parser.parse_args()

#show debugging prints?
#0 - don't show debugging stuff and perform actual run through effect comments
#1 - show only for first iteration
#2 - show for all iterations
debugLevel = options.debug

######################### Control #########################
#Ways to control process:
#Adjust grouping type weights (more number - better chance to pick this
#grouping type)
groupWeight = 1.0
categoryWeight = 1.0
baseTypeWeight = 1.0
marketGroupWithVarsWeight = 0.7
typeNameCombinationWeight = 1.0
#If score drops below this value, remaining items will be
#listed without any grouping
lowestScore = 0.7
#Adjust inner/outer score calculation formulae
def calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected, weight = 1.0):
    innerAffectedPortionDescribed = affectedAndDecribed/total
    innerAffectedPortionUndescribed = affectedAndUndescribed/total
    #Items which are already described have 0 weight for now
    innerScore = (innerAffectedPortionUndescribed + innerAffectedPortionDescribed*0)*(affectedAndDecribed+affectedAndUndescribed-1)*weight
    return innerScore
def calcOuterScore(innerScoreDict, perEffect_totalAffected, weight):
    #Return just max of the inner scores, including weight factor
    if float(len(innerScoreDict)):
        return innerScoreDict[max(innerScoreDict, key = lambda a: innerScoreDict.get(a))] * weight
    else: return 0.0

#Connect to database and set up cursor
db = sqlite3.connect(os.path.expanduser(options.database))
cursor = db.cursor()

#As we don't rely on pyfa's overrides, we need to set them manually
overrides = '''
UPDATE invtypes SET published = '1' WHERE typeName = 'Freki';
UPDATE invtypes SET published = '1' WHERE typeName = 'Mimir';
UPDATE invtypes SET published = '1' WHERE typeName = 'Utu';
UPDATE invtypes SET published = '1' WHERE typeName = 'Adrestia';
'''
for statement in overrides.split(";\n"):
    cursor.execute(statement)

#List of queries which will be used in the script
queryAllEffects = 'SELECT dgmeffects.effectID, dgmeffects.effectName FROM dgmeffects'
#Queries to get raw data
#Limit categories to Celestials (2, only for wormhole effects), Ships (6), Modules (7), Charges (8), Skills (16), Drones (18), Implants (2), Subsystems (32)
categoryLimiter = ' AND (invcategories.categoryID = 2 OR invcategories.categoryID = 6 OR invcategories.categoryID = 7 OR invcategories.categoryID = 8 OR invcategories.categoryID = 16 OR invcategories.categoryID = 18 OR invcategories.categoryID = 20 OR invcategories.categoryID = 32)'
queryPublishedTypeIDs = 'SELECT invtypes.typeID FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryTypeIDGroupID = 'SELECT invtypes.groupID FROM invtypes WHERE invtypes.typeID = ? LIMIT 1'
queryGroupIDCategoryID = 'SELECT invgroups.categoryID FROM invgroups WHERE invgroups.groupID = ? LIMIT 1'
queryTypeIDParentTypeID = 'SELECT invmetatypes.parentTypeID FROM invmetatypes WHERE invmetatypes.typeID = ? LIMIT 1'
queryTypeIDMarketGroupID = 'SELECT invtypes.marketGroupID FROM invtypes WHERE invtypes.typeID = ? LIMIT 1'
queryTypeIDTypeName = 'SELECT invtypes.typeName FROM invtypes WHERE invtypes.typeID = ? LIMIT 1'
queryMarketGroupIDParentGroupID = 'SELECT invmarketgroups.parentGroupID FROM invmarketgroups WHERE invmarketgroups.marketGroupID = ? LIMIT 1'
queryEffectIDTypeID = 'SELECT dgmtypeeffects.typeID FROM dgmtypeeffects WHERE dgmtypeeffects.effectID = ?'
#Queries for printing
queryGroupName = 'SELECT invgroups.groupName FROM invgroups WHERE invgroups.groupID = ? LIMIT 1'
queryCategoryName = 'SELECT invcategories.categoryName FROM invcategories WHERE invcategories.categoryID = ? LIMIT 1'
queryMarketGroupName = 'SELECT invmarketgroups.marketGroupName FROM invmarketgroups WHERE invmarketgroups.marketGroupID = ? LIMIT 1'

#Compose list of effects w/o symbols which pyfa doesn't take into consideration
#we'll use it to find proper effect IDs from file names
globalMap_effectNamePyfa_effectNameDB = {}
stripSpec = "[^A-Za-z0-9]"
cursor.execute(queryAllEffects)
for row in cursor:
    globalMap_effectNamePyfa_effectNameDB[re.sub(stripSpec, "", row[1])] = row[0]

######################### Stage 1 #########################

#Published types set
publishedTypes = set()
cursor.execute(queryPublishedTypeIDs)
for row in cursor:
    publishedTypes.add(row[0])

#Compose group maps
# { groupID : set(typeID) }
globalMap_groupID_typeID = {}
# { typeID : groupID }
globalMap_typeID_groupID = {}
for typeID in publishedTypes:
    groupID = 0
    cursor.execute(queryTypeIDGroupID, (typeID,))
    for row in cursor: groupID = row[0]
    if not groupID in globalMap_groupID_typeID: globalMap_groupID_typeID[groupID] = set()
    globalMap_groupID_typeID[groupID].add(typeID)
    globalMap_typeID_groupID[typeID] = groupID

#Category maps
# { categoryID : set(typeID) }
globalMap_categoryID_typeID =  {}
# { typeID : categoryID }
globalMap_typeID_categoryID =  {}
for typeID in publishedTypes:
    categoryID = 0
    cursor.execute(queryGroupIDCategoryID, (globalMap_typeID_groupID[typeID],))
    for row in cursor: categoryID = row[0]
    if not categoryID in globalMap_categoryID_typeID: globalMap_categoryID_typeID[categoryID] = set()
    globalMap_categoryID_typeID[categoryID].add(typeID)
    globalMap_typeID_categoryID[typeID] = categoryID

#BaseType maps
# { baseTypeID : set(typeID) }
globalMap_baseTypeID_typeID =  {}
# { typeID : baseTypeID }
globalMap_typeID_baseTypeID =  {}
for typeID in publishedTypes:
    #not all items in the database have baseTypeIDs, so
    #assign some default value to it
    baseTypeID = 0
    cursor.execute(queryTypeIDParentTypeID, (typeID,))
    for row in cursor: baseTypeID = row[0]
    #if baseType is not published or is not set in database,
    #consider item as variation of self
    if baseTypeID not in publishedTypes: baseTypeID = typeID
    if not baseTypeID in globalMap_baseTypeID_typeID: globalMap_baseTypeID_typeID[baseTypeID] = set()
    globalMap_baseTypeID_typeID[baseTypeID].add(typeID)
    globalMap_typeID_baseTypeID[typeID] = baseTypeID

#MarketGroup maps. We won't use this one for further processing,
#just as helper for composing other maps
# { marketGroupID : set(typeID) }
globalMap_marketGroupID_typeID =  {}
# { typeID : set(marketGroupID) }
globalMap_typeID_marketGroupID =  {}
for typeID in publishedTypes:
    marketGroupID = 0
    cursor.execute(queryTypeIDMarketGroupID, (typeID,))
    for row in cursor: marketGroupID = row[0]
    if not marketGroupID: continue
    if not marketGroupID in globalMap_marketGroupID_typeID: globalMap_marketGroupID_typeID[marketGroupID] = set()
    globalMap_marketGroupID_typeID[marketGroupID].add(typeID)
#Copy items to all parent market groups
intialMarketGroupIDList = []
for marketGroupID in globalMap_marketGroupID_typeID: intialMarketGroupIDList.append(marketGroupID)
for marketGroupID in intialMarketGroupIDList:
    #Limit depths for case if database will refer to groups making the loop
    cyclingMarketGroupID = marketGroupID
    for depth in range(20):
        cursorParentMarket = db.cursor()
        cursorParentMarket.execute(queryMarketGroupIDParentGroupID, (cyclingMarketGroupID,))
        for row in cursorParentMarket:
            cyclingMarketGroupID = row[0]
        if cyclingMarketGroupID:
            if not cyclingMarketGroupID in globalMap_marketGroupID_typeID: globalMap_marketGroupID_typeID[cyclingMarketGroupID] = set()
            globalMap_marketGroupID_typeID[cyclingMarketGroupID] |= globalMap_marketGroupID_typeID[marketGroupID]
        else: break
#Now, make a reverse map
for marketGroupID, typeIDSet in globalMap_marketGroupID_typeID.items():
    for typeID in typeIDSet:
        if not typeID in globalMap_typeID_marketGroupID: globalMap_typeID_marketGroupID[typeID] = set()
        globalMap_typeID_marketGroupID[typeID].add(marketGroupID)

#Combining market groups and variations
# { marketGroupID : set(typeIDWithVariations) }
globalMap_marketGroupID_typeIDWithVariations = copy.deepcopy(globalMap_marketGroupID_typeID)
# { typeIDWithVariations : set(marketGroupID) }
globalMap_typeIDWithVariations_marketGroupID = {}
for marketGroupID in globalMap_marketGroupID_typeIDWithVariations:
    typesToAdd = set()
    for typeID in globalMap_marketGroupID_typeIDWithVariations[marketGroupID]:
        if typeID in globalMap_baseTypeID_typeID:
            for variationID in globalMap_baseTypeID_typeID[typeID]:
                #Do not include items which have market group, even if they're variation
                if variationID in globalMap_typeID_marketGroupID: typesToAdd.add(variationID)
    globalMap_marketGroupID_typeIDWithVariations[marketGroupID] |= typesToAdd
#Make reverse map using simple way too
for marketGroupID, typeIDWithVariationsSet in globalMap_marketGroupID_typeIDWithVariations.items():
    for typeID in typeIDWithVariationsSet:
        if not typeID in globalMap_typeIDWithVariations_marketGroupID: globalMap_typeIDWithVariations_marketGroupID[typeID] = set()
        globalMap_typeIDWithVariations_marketGroupID[typeID].add(marketGroupID)

#Item names map
#We need to include category ID to avoid combining items from
#different categories (e.g. skills and modules)
# { ((typeNameCombination), categoryID) : set(typeID) }
globalMap_typeNameCombinationTuple_typeID =  {}
# { typeID : (set((typeNameCombination)), len(typeName)) }
globalMap_typeID_typeNameCombination =  {}
for typeID in publishedTypes:
    typeName = ""
    cursor.execute(queryTypeIDTypeName, (typeID,))
    for row in cursor: typeName = row[0]
    #Let's split strings into separate words
    typeNameSplitted = []
    #Start from the whole typeName
    remainingString = typeName
    #We will pick word each iteration
    iterate = True
    while iterate:
        #This regexp helps to split into words with spaces and dashes between them
        #For example: CX|-|1, Hardwiring| - |Inherent, Zainou| |'Snapshot'
        separatingPatternGeneral = "((?P<left_part>[^ -]+)(?P<separator>[ -]+)(?P<right_part>([^ -].*)))"
        #This will help to split names like those used in implants, for exapmle ZET||500, EE||8
        separatingPatternSeries = "((?P<left_part>[A-Za-z]{2,4})(?P<right_part>[0-9]{1,4}.*))"
        #Check remaining string using both criteria
        matchObjectGeneral = re.match(separatingPatternGeneral, remainingString)
        matchObjectSeries = re.match(separatingPatternSeries, remainingString)
        #Now, we need to find which criterion satisfies us
        useGeneral = False
        useSeries = False
        #If remaining string meets both criteria
        if matchObjectGeneral and matchObjectSeries:
            #We check which occurs first and pick it
            if len(matchObjectGeneral.group("left_part")) <= len(matchObjectSeries.group("left_part")): useGeneral = True
            else: useSeries = True
        #If only one criterion is met, just pick it
        elif matchObjectGeneral:
            useGeneral = True
        elif matchObjectSeries:
            useSeries = True
        #Now, actually split string into word, separator and remaining string
        #And append word to list of words of current typeName
        if useGeneral:
            newWord = matchObjectGeneral.group("left_part")
            separator = matchObjectGeneral.group("separator")
            remainingString = matchObjectGeneral.group("right_part")
            typeNameSplitted.append(newWord)
        elif useSeries:
            newWord = matchObjectSeries.group("left_part")
            separator = ""
            remainingString = matchObjectSeries.group("right_part")
            typeNameSplitted.append(newWord)
        #If we didn't match any regexp, then we see last word.
        #Append it too and stop iterating
        else:
            typeNameSplitted.append(remainingString)
            iterate = False
    #Iterate  through number of words which will be used to compose combinations
    for wordNumIndex in range(len(typeNameSplitted)):
        #Iterate through all possible combinations
        for typeNameCombination in itertools.combinations(typeNameSplitted, wordNumIndex + 1):
            typeNameCombinationTuple = (typeNameCombination, globalMap_typeID_categoryID[typeID])
            if not typeNameCombinationTuple in globalMap_typeNameCombinationTuple_typeID: globalMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple] = set()
            globalMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple].add(typeID)
            if not typeID in globalMap_typeID_typeNameCombination: globalMap_typeID_typeNameCombination[typeID] = (set(), len(typeNameSplitted))
            globalMap_typeID_typeNameCombination[typeID][0].add(typeNameCombination)

######################### Stage 2 #########################
#Go through effect files one-by-one
effectsPath = os.path.join("..", "effects")
for effectFileName in os.listdir(effectsPath):
    basename, extension = effectFileName.split('.')
    #Ignore non-py files and exclude implementation-specific 'effects'
    if extension == "py" and not basename in ("__init__"):
        ######################## Stage 2.1 ########################
        #Data regarding which items are effected by current effect
        perEffectList_usedByTypes = set()
        cursor.execute(queryEffectIDTypeID, (globalMap_effectNamePyfa_effectNameDB[basename],))
        for rowTypes in cursor:
            typeID = rowTypes[0]
            if typeID in publishedTypes: perEffectList_usedByTypes.add(typeID)
        #Number of items affected by current effect
        perEffect_totalAffected = len(perEffectList_usedByTypes)

        #Compose per-group map of items which are affected by current effect
        # { groupID : (set(typeID), describes) }
        perEffectMap_groupID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            groupID = globalMap_typeID_groupID[typeID]
            if not groupID in perEffectMap_groupID_typeID: perEffectMap_groupID_typeID[groupID] = [set(), False]
            perEffectMap_groupID_typeID[groupID][0].add(typeID)

        #Now, per-category map of items
        # { categoryID : (set(typeID), describes) }
        perEffectMap_categoryID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            categoryID = globalMap_typeID_categoryID[typeID]
            if not categoryID in perEffectMap_categoryID_typeID: perEffectMap_categoryID_typeID[categoryID] = [set(), False]
            perEffectMap_categoryID_typeID[categoryID][0].add(typeID)

        #Per-baseType map of variations
        # { baseTypeID : (set(typeID), describes) }
        perEffectMap_baseTypeID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            baseTypeID = globalMap_typeID_baseTypeID[typeID]
            if not baseTypeID in perEffectMap_baseTypeID_typeID: perEffectMap_baseTypeID_typeID[baseTypeID] = [set(), False]
            perEffectMap_baseTypeID_typeID[baseTypeID][0].add(typeID)

        #Per-marketGroup map with variations
        # { marketGroupID : (set(typeIDWithVariations), describes) }
        perEffectMap_marketGroupID_typeIDWithVariations = {}
        for typeID in perEffectList_usedByTypes:
            if typeID in globalMap_typeID_marketGroupID: marketGroupIDs = globalMap_typeID_marketGroupID[typeID]
            else: marketGroupIDs = set()
            for marketGroupID in marketGroupIDs:
                if not marketGroupID in perEffectMap_marketGroupID_typeIDWithVariations: perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID] = [set(), False]
                perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID][0].add(typeID)

        #Per-typeNameCombination map
        # { ((typeNameCombination), categoryID) : (set(typeID), describes) }
        perEffectMap_typeNameCombinationTuple_typeID = {}
        for typeID in perEffectList_usedByTypes:
            typeNameCombinations = globalMap_typeID_typeNameCombination[typeID][0]
            for typeNameCombination in typeNameCombinations:
                typeNameCombinationTuple = (typeNameCombination, globalMap_typeID_categoryID[typeID])
                if not typeNameCombinationTuple in perEffectMap_typeNameCombinationTuple_typeID: perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple] = [set(), False]
                perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple][0].add(typeID)

        stopDebugPrints = False
        if debugLevel >= 1:
            print("\nEffect:", basename)
            print("Total items affected: {0}".format(perEffect_totalAffected))

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
                    affectedAndDecribed = len(affectedItemsFromCurrentGroup.intersection(perEffect_describedTypes))
                    #yet undescribed
                    affectedAndUndescribed =  len(affectedItemsFromCurrentGroup.difference(perEffect_describedTypes))
                    #total number of items from this group (not necessarily affected by current effect)
                    total = len(globalMap_groupID_typeID[groupID])
                    #calculate inner score and push it into score dictionary for current grouping type
                    groupScore[groupID] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected)
                    #Debug prints for inner data
                    if debugLevel >= 1 and not stopDebugPrints:
                        cursor.execute(queryGroupName, (groupID,))
                        for row in cursor: groupName = row[0]
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        #If debug level is 1, we print results only for 1st iteration
                        if debugLevel == 1: print("Group: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(groupName, affectedAndUndescribed, total, coverage, groupScore[groupID]))
                        #If it's 2, we print results for each iteration, so we need to
                        #include number of already described items
                        if debugLevel == 2: print("Group: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(groupName, affectedAndUndescribed, affectedAndDecribed, total, coverage, groupScore[groupID]))
            #Calculate outer score for this grouping type
            groupOuterScore = calcOuterScore(groupScore, perEffect_totalAffected, groupWeight)
            #Debug print for outer data
            if debugLevel >= 1 and not stopDebugPrints: print("Groups outer score: {0:.3}".format(groupOuterScore))

            categoryScore = {}
            for categoryID in perEffectMap_categoryID_typeID:
                if not perEffectMap_categoryID_typeID[categoryID][1]:
                    affectedItemsFromCurrentCategory = perEffectMap_categoryID_typeID[categoryID][0]
                    affectedAndDecribed = len(affectedItemsFromCurrentCategory.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrentCategory.difference(perEffect_describedTypes))
                    total = len(globalMap_categoryID_typeID[categoryID])
                    categoryScore[categoryID] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected)
                    if debugLevel >= 1 and not stopDebugPrints:
                        cursor.execute(queryCategoryName, (categoryID,))
                        for row in cursor: categoryName = row[0]
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Category: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(categoryName, affectedAndUndescribed, total, coverage, categoryScore[categoryID]))
                        if debugLevel == 2: print("Category: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(categoryName, affectedAndUndescribed, affectedAndDecribed, total, coverage, categoryScore[categoryID]))
            categoryOuterScore = calcOuterScore(categoryScore, perEffect_totalAffected, categoryWeight)
            if debugLevel >= 1 and not stopDebugPrints: print("Category outer score: {0:.3}".format(categoryOuterScore))

            baseTypeScore = {}
            for baseTypeID in perEffectMap_baseTypeID_typeID:
                if not perEffectMap_baseTypeID_typeID[baseTypeID][1]:
                    affectedItemsFromCurrentBaseType = perEffectMap_baseTypeID_typeID[baseTypeID][0]
                    affectedAndDecribed = len(affectedItemsFromCurrentBaseType.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrentBaseType.difference(perEffect_describedTypes))
                    total = len(globalMap_baseTypeID_typeID[baseTypeID])
                    baseTypeScore[baseTypeID] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected)
                    if debugLevel >= 1 and not stopDebugPrints:
                        cursor.execute(queryTypeIDTypeName, (baseTypeID,))
                        for row in cursor: baseTypeName = row[0]
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Base item: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(baseTypeName, affectedAndUndescribed, total, coverage, baseTypeScore[baseTypeID]))
                        if debugLevel == 2: print("Base item: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(baseTypeName, affectedAndUndescribed, affectedAndDecribed, total, coverage, baseTypeScore[baseTypeID]))
            baseTypeOuterScore = calcOuterScore(baseTypeScore, perEffect_totalAffected, baseTypeWeight)
            #Print outer data
            if debugLevel >= 1 and not stopDebugPrints: print("Base item outer score: {0:.3}".format(baseTypeOuterScore))

            marketGroupWithVarsScore = {}
            for marketGroupID in perEffectMap_marketGroupID_typeIDWithVariations:
                if not perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID][1]:
                    affectedItemsFromCurrentMarketGroupWithVars = perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID][0]
                    affectedAndDecribed = len(affectedItemsFromCurrentMarketGroupWithVars.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrentMarketGroupWithVars.difference(perEffect_describedTypes))
                    total = len(globalMap_marketGroupID_typeIDWithVariations[marketGroupID])
                    marketGroupWithVarsScore[marketGroupID] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected)
                    if debugLevel >= 1 and not stopDebugPrints:
                        cursor.execute(queryMarketGroupName, (marketGroupID,))
                        for row in cursor: marketGroupName = row[0]
                        #Prepend market group name with its parents names
                        prependParentID = marketGroupID
                        #Limit depth in case if market groups form a loop
                        for depth in range(20):
                            cursorParentMarket = db.cursor()
                            cursorParentMarket.execute(queryMarketGroupIDParentGroupID, (prependParentID,))
                            for row in cursorParentMarket:
                                prependParentID = row[0]
                            if prependParentID:
                                cursor.execute(queryMarketGroupName, (prependParentID,))
                                for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                            else: break
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Market group with variations: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(marketGroupName, affectedAndUndescribed, total, coverage, marketGroupWithVarsScore[marketGroupID]))
                        if debugLevel == 2: print("Market group with variations: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(marketGroupName, affectedAndUndescribed, affectedAndDecribed, total, coverage, marketGroupWithVarsScore[marketGroupID]))
            marketGroupWithVarsOuterScore = calcOuterScore(marketGroupWithVarsScore, perEffect_totalAffected, marketGroupWithVarsWeight)
            if debugLevel >= 1 and not stopDebugPrints: print("Market group outer score: {0:.3}".format(marketGroupWithVarsOuterScore))

            typeNameCombinationScore = {}
            for typeNameCombinationTuple in perEffectMap_typeNameCombinationTuple_typeID:
                if not perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple][1]:
                    affectedItemsFromCurrenttypeNameCombination = perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple][0]
                    affectedAndDecribed = len(affectedItemsFromCurrenttypeNameCombination.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrenttypeNameCombination.difference(perEffect_describedTypes))
                    total = len(globalMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple])
                    #typeNames are special: wee also need to consider how certain
                    #word combination covers full typeName. We start from zero
                    averageCoverage = 0
                    itemsNamedLikeThis = perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationTuple][0]
                    for typeID in itemsNamedLikeThis:
                        #Add number of words in combination divided by total number of words from any given item
                        averageCoverage += len(typeNameCombinationTuple[0])/globalMap_typeID_typeNameCombination[typeID][1]
                    #Then divide by number of items we checked, making it real average
                    averageCoverage = averageCoverage/len(itemsNamedLikeThis)
                    #Pass average coverage as additional balancing factor
                    typeNameCombinationScore[typeNameCombinationTuple] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected, 0.2 + averageCoverage*0.8)
                    if debugLevel >= 1 and not stopDebugPrints:
                        typeNameCombinationPrintable = " ".join(typeNameCombinationTuple[0])
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Type name combination: \"{0}\": {1}/{2} ({3:.3}%, inner score: {4:.3})".format(typeNameCombinationPrintable, affectedAndUndescribed, total, coverage, typeNameCombinationScore[typeNameCombinationTuple]))
                        if debugLevel == 2: print("Type name combination: \"{0}\": {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(typeNameCombinationPrintable, affectedAndUndescribed, affectedAndDecribed, total, coverage, typeNameCombinationScore[typeNameCombinationTuple]))
            typeNameCombinationOuterScore = calcOuterScore(typeNameCombinationScore, perEffect_totalAffected, typeNameCombinationWeight)
            if debugLevel >= 1 and not stopDebugPrints: print("Type name combination outer score: {0:.3}".format(typeNameCombinationOuterScore))

            #Don't print anything after 1st iteration at 1st debugging level
            if debugLevel == 1: stopDebugPrints = True
            #Print separator for 2nd debugging level, to separate debug data of one
            #iteration from another
            if debugLevel >= 2: print("---")

            ####################### Stage 2.2.2 #######################
            #Pick max score from outer scores of all grouping types
            maxOuterScore = max(groupOuterScore, categoryOuterScore, baseTypeOuterScore, marketGroupWithVarsOuterScore, typeNameCombinationOuterScore)
            #define lower limit for score, below which there will be no winners
            if maxOuterScore >= lowestScore:
                #If scores are similar, priorities are: category > group > name > marketGroup > baseType
                if maxOuterScore == categoryOuterScore:
                    #pick ID of category which has highest score among other categories
                    categoryWinner = max(categoryScore, key=categoryScore.get)
                    #Add it to the list of categories which describe set of items
                    describedByCategory.append(categoryWinner)
                    #add all items described by winning category into set of described items
                    perEffect_describedTypes |= globalMap_categoryID_typeID[categoryWinner]
                    #set 'describes' flag to avoid processing of this category
                    #during following iterations
                    perEffectMap_categoryID_typeID[categoryWinner][1] = True
                elif maxOuterScore == groupOuterScore:
                    groupWinner = max(groupScore, key=groupScore.get)
                    describedByGroup.append(groupWinner)
                    perEffect_describedTypes |= globalMap_groupID_typeID[groupWinner]
                    perEffectMap_groupID_typeID[groupWinner][1] = True
                elif maxOuterScore == typeNameCombinationOuterScore:
                    typeNameCombinationWinner = max(typeNameCombinationScore, key=typeNameCombinationScore.get)
                    describedByTypeNameCombination.append(typeNameCombinationWinner)
                    perEffect_describedTypes |= globalMap_typeNameCombinationTuple_typeID[typeNameCombinationWinner]
                    perEffectMap_typeNameCombinationTuple_typeID[typeNameCombinationWinner][1] = True
                elif maxOuterScore == marketGroupWithVarsOuterScore:
                    marketGroupWithVarsWinner = max(marketGroupWithVarsScore, key=marketGroupWithVarsScore.get)
                    describedByMarketGroupWithVars.append(marketGroupWithVarsWinner)
                    perEffect_describedTypes |= globalMap_marketGroupID_typeIDWithVariations[marketGroupWithVarsWinner]
                    perEffectMap_marketGroupID_typeIDWithVariations[marketGroupWithVarsWinner][1] = True
                elif maxOuterScore == baseTypeOuterScore:
                    baseTypeWinner = max(baseTypeScore, key=baseTypeScore.get)
                    describedByBaseType.append(baseTypeWinner)
                    perEffect_describedTypes |= globalMap_baseTypeID_typeID[baseTypeWinner]
                    perEffectMap_baseTypeID_typeID[baseTypeWinner][1] = True
            #Stop if we have score less than some critical value, all undescribed
            #items will be provided as plain list
            else: iterate = False
            #Also stop if we described all items
            if perEffectList_usedByTypes.issubset(perEffect_describedTypes): iterate = False
        singleItems = set(perEffectList_usedByTypes).difference(perEffect_describedTypes)
        if debugLevel >= 1:
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
        for typeID in singleItems:
            typeName = ""
            cursor.execute(queryTypeIDTypeName, (typeID,))
            for row in cursor: typeName = row[0]
            categoryName = ""
            cursor.execute(queryCategoryName, (globalMap_typeID_categoryID[typeID],))
            for row in cursor: categoryName = row[0]
            printing_types.append((typeID, typeName, categoryName))
        for groupID in describedByGroup:
            groupName = ""
            cursor.execute(queryGroupName, (groupID,))
            for row in cursor: groupName = row[0]
            categoryID = 0
            cursor.execute(queryGroupIDCategoryID, (groupID,))
            for row in cursor: categoryID = row[0]
            categoryName = ""
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            printing_groups.append((groupID, groupName, categoryName))
        for categoryID in describedByCategory:
            categoryName = ""
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            printing_categories.append((categoryID, categoryName))
        for baseTypeID in describedByBaseType:
            baseTypeName = ""
            cursor.execute(queryTypeIDTypeName, (baseTypeID,))
            for row in cursor: baseTypeName = row[0]
            categoryName = ""
            cursor.execute(queryCategoryName, (globalMap_typeID_categoryID[baseTypeID],))
            for row in cursor: categoryName = row[0]
            printing_baseTypes.append((baseTypeID, baseTypeName, categoryName))
        for marketGroupID in describedByMarketGroupWithVars:
            cursor.execute(queryMarketGroupName, (marketGroupID,))
            for row in cursor: marketGroupName = row[0]
            #Prepend market group name with its parents names
            prependParentID = marketGroupID
            #Limit depth to avoid looping, as usual
            for depth in range(20):
                cursorParentMarket = db.cursor()
                cursorParentMarket.execute(queryMarketGroupIDParentGroupID, (prependParentID,))
                for row in cursorParentMarket:
                    prependParentID = row[0]
                if prependParentID:
                    cursor.execute(queryMarketGroupName, (prependParentID,))
                    for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                else: break
            printing_marketGroupsWithVars.append((marketGroupID, marketGroupName))
        for typeNameCombinationTuple in describedByTypeNameCombination:
            typeNameCombinationPrint = " ".join(typeNameCombinationTuple[0])
            categoryName = ""
            cursor.execute(queryCategoryName, (typeNameCombinationTuple[1],))
            for row in cursor: categoryName = row[0]
            printing_typeNameCombinationTuples.append((typeNameCombinationTuple, typeNameCombinationPrint, categoryName))

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
            printing_groupLines.append("#{0}s from group: {1} ({2} of {3})".format(group[2], group[1], len(perEffectMap_groupID_typeID[group[0]][0]), len(globalMap_groupID_typeID[group[0]])))
        printing_categoryLines = []
        printing_categories = sorted(printing_categories, key=lambda tuple: tuple[1])
        for category in printing_categories:
            printing_categoryLines.append("#Items from category: {0} ({1} of {2})".format(category[1], len(perEffectMap_categoryID_typeID[category[0]][0]), len(globalMap_categoryID_typeID[category[0]])))
        printing_baseTypeLines = []
        printing_baseTypes = sorted(printing_baseTypes, key=lambda tuple: tuple[1])
        printing_baseTypes = sorted(printing_baseTypes, key=lambda tuple: tuple[2])
        for baseType in printing_baseTypes:
            printing_baseTypeLines.append("#Variations of {0}: {1} ({2} of {3})".format(baseType[2].lower(), baseType[1], len(perEffectMap_baseTypeID_typeID[baseType[0]][0]), len(globalMap_baseTypeID_typeID[baseType[0]])))
        printing_marketGroupWithVarsLines = []
        printing_marketGroupsWithVars = sorted(printing_marketGroupsWithVars, key=lambda tuple: tuple[1])
        for marketGroup in printing_marketGroupsWithVars:
            printing_marketGroupWithVarsLines.append("#Items from market group: {0} ({1} of {2})".format(marketGroup[1], len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroup[0]][0]), len(globalMap_marketGroupID_typeIDWithVariations[marketGroup[0]])))
        printing_typeNameCombinationTupleLines = []
        printing_typeNameCombinationTuples = sorted(printing_typeNameCombinationTuples, key=lambda tuple: tuple[1])
        printing_typeNameCombinationTuples = sorted(printing_typeNameCombinationTuples, key=lambda tuple: tuple[2])
        for typeNameCombination in printing_typeNameCombinationTuples:
            printing_typeNameCombinationTupleLines.append("#{0}s named like: {1} ({2} of {3})".format(typeNameCombination[2], typeNameCombination[1], len(perEffectMap_typeNameCombinationTuple_typeID[typeNameCombination[0]][0]), len(globalMap_typeNameCombinationTuple_typeID[typeNameCombination[0]])))

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
        if debugLevel == 0 and (effectContentsProcessed != effectContentsSource):
            effectFile = open(os.path.join(effectsPath, effectFileName), 'w')
            effectFile.write(effectContentsProcessed)
            effectFile.close()
        elif debugLevel >= 2:
            print("Comment to write to file:")
            print("\n".join(commentLines))
