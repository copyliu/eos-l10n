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

import sqlite3
import os.path
import re
import math
import itertools
import copy

#show debugging prints?
#0 - don't show debugging stuff and perform actual run through effect comments
#1 - show only for first iteration
#2 - show for all iterations
debugLevel = 0

#Connect to database and set up cursor
db = sqlite3.connect(os.path.expanduser(os.path.join("~", ".pyfa","eve.db")))
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
#Limit categories to Celestials (2, only for wormhole effects), Ships (6), Modules (7), Charges (8), Skills (16), Drones (18), Implants (2), Subsystems (32)
categoryLimiter = ' AND (invcategories.categoryID = 2 OR invcategories.categoryID = 6 OR invcategories.categoryID = 7 OR invcategories.categoryID = 8 OR invcategories.categoryID = 16 OR invcategories.categoryID = 18 OR invcategories.categoryID = 20 OR invcategories.categoryID = 32)'
queryAllEffects = 'SELECT dgmeffects.effectID, dgmeffects.effectName FROM dgmeffects'
queryPublishedTypes = 'SELECT invtypes.typeID, invtypes.groupID FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryPublishedTypeCategories = 'SELECT invtypes.typeID, invgroups.categoryID FROM invtypes  INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryPublishedTypeVariations = 'SELECT invmetatypes.typeID, invmetatypes.parentTypeID FROM invmetatypes INNER JOIN invtypes ON invmetatypes.typeID = invtypes.typeID INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryPublishedSelfVariations = 'SELECT invtypes.typeID FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1 AND invtypes.typeID NOT IN (SELECT invmetatypes.typeID FROM invmetatypes)' + categoryLimiter
queryPublishedTypeMarketGroups = 'SELECT invtypes.typeID, invtypes.marketGroupID FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryPublishedTypeNames = 'SELECT invtypes.typeID, invtypes.typeName FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1' + categoryLimiter
queryMarketGroupRelations = 'SELECT invmarketgroups.marketGroupID, invmarketgroups.parentGroupID FROM invmarketgroups'
queryTypesUsedByEffect = 'SELECT invtypes.typeID FROM invtypes INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID INNER JOIN dgmtypeeffects ON dgmtypeeffects.typeID = invtypes.typeID INNER JOIN dgmeffects ON dgmeffects.effectID = dgmtypeeffects.effectID WHERE invtypes.published = 1' + categoryLimiter + ' AND dgmeffects.effectID = ?'
queryParentMarketGroup = 'SELECT invmarketgroups.parentGroupID FROM invmarketgroups WHERE invmarketgroups.marketGroupID = ? LIMIT 1'
queryGroupCategory = 'SELECT invgroups.categoryID FROM invgroups WHERE invgroups.groupID = ? LIMIT 1'
queryTypeName = 'SELECT invtypes.typeName FROM invtypes WHERE invtypes.typeID = ? LIMIT 1'
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
#Compose group maps
# { groupID : set(typeID) }
globalMap_groupID_typeID = {}
# { typeID : groupID }
globalMap_typeID_groupID = {}
cursor.execute(queryPublishedTypes)
for row in cursor:
    typeID, groupID = row[0], row[1]
    if not groupID in globalMap_groupID_typeID: globalMap_groupID_typeID[groupID] = set()
    globalMap_groupID_typeID[groupID].add(typeID)
    globalMap_typeID_groupID[typeID] = groupID

#Category maps
# { categoryID : set(typeID) }
globalMap_categoryID_typeID =  {}
# { typeID : categoryID }
globalMap_typeID_categoryID =  {}
cursor.execute(queryPublishedTypeCategories)
for row in cursor:
    typeID, categoryID = row[0], row[1]
    if not categoryID in globalMap_categoryID_typeID: globalMap_categoryID_typeID[categoryID] = set()
    globalMap_categoryID_typeID[categoryID].add(typeID)
    globalMap_typeID_categoryID[typeID] = categoryID

#BaseType maps
# { baseTypeID : set(typeID) }
globalMap_baseTypeID_typeID =  {}
# { typeID : baseTypeID }
globalMap_typeID_baseTypeID =  {}
cursor.execute(queryPublishedTypeVariations)
for row in cursor:
    typeID, baseTypeID = row[0], row[1]
    if not baseTypeID in globalMap_baseTypeID_typeID: globalMap_baseTypeID_typeID[baseTypeID] = set()
    globalMap_baseTypeID_typeID[baseTypeID].add(typeID)
    globalMap_typeID_baseTypeID[typeID] = baseTypeID
#All items which do not have base item are considered as variations of self
cursor.execute(queryPublishedSelfVariations)
for row in cursor:
    typeID = row[0]
    if not typeID in globalMap_baseTypeID_typeID: globalMap_baseTypeID_typeID[typeID] = set()
    globalMap_baseTypeID_typeID[typeID].add(typeID)
    globalMap_typeID_baseTypeID[typeID] = typeID

#MarketGroup maps. We won't use this one for further processing,
#just as helper for composing other maps
# { marketGroupID : set(typeID) }
globalMap_marketGroupID_typeID =  {}
# { typeID : set(marketGroupID) }
globalMap_typeID_marketGroupID =  {}
cursor.execute(queryPublishedTypeMarketGroups)
for row in cursor:
    typeID, marketGroupID = row[0], row[1]
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
        cursorParentMarket.execute(queryParentMarketGroup, (cyclingMarketGroupID,))
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
# { (typeNameCombination) : set(typeID) }
globalMap_typeNameCombination_typeID =  {}
# { typeID : (set((typeNameCombination)), len(typeName)) }
globalMap_typeID_typeNameCombination =  {}
cursor.execute(queryPublishedTypeNames)
for row in cursor:
    typeID, typeName = row[0], row[1]
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
            if not typeNameCombination in globalMap_typeNameCombination_typeID: globalMap_typeNameCombination_typeID[typeNameCombination] = set()
            globalMap_typeNameCombination_typeID[typeNameCombination].add(typeID)
            if not typeID in globalMap_typeID_typeNameCombination: globalMap_typeID_typeNameCombination[typeID] = (set(), len(typeNameSplitted))
            globalMap_typeID_typeNameCombination[typeID][0].add(typeNameCombination)

#Method for calculating score of group inside set of groups of given type
def calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected, weight = 1.0):
    innerAffectedPortionDescribed = affectedAndDecribed/total
    innerAffectedPortionUndescribed = affectedAndUndescribed/total
    #Items which are already described have 0 weight for now
    innerScore = (innerAffectedPortionUndescribed + innerAffectedPortionDescribed*0)*(affectedAndDecribed+affectedAndUndescribed-1)*weight
    return innerScore

#Method for calculating score of group types
def calcOuterScore(innerScoreDict, perEffect_totalAffected, weight):
    #Return just max of the inner scores, including weight factor
    if float(len(innerScoreDict)):
        return innerScoreDict[max(innerScoreDict, key = lambda a: innerScoreDict.get(a))] * weight
    else: return 0.0

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
        cursor.execute(queryTypesUsedByEffect, (globalMap_effectNamePyfa_effectNameDB[basename],))
        for rowTypes in cursor:
            typeID = rowTypes[0]
            perEffectList_usedByTypes.add(typeID)
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
        # { typeNameCombination : (set(typeID), describes) }
        perEffectMap_typeNameCombination_typeID = {}
        for typeID in perEffectList_usedByTypes:
            typeNameCombinations = globalMap_typeID_typeNameCombination[typeID][0]
            for typeNameCombination in typeNameCombinations:
                if not typeNameCombination in perEffectMap_typeNameCombination_typeID: perEffectMap_typeNameCombination_typeID[typeNameCombination] = [set(), False]
                perEffectMap_typeNameCombination_typeID[typeNameCombination][0].add(typeID)

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
            groupWeight = 1.0
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
            categoryWeight = 1.0
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
            baseTypeWeight = 1.0
            for baseTypeID in perEffectMap_baseTypeID_typeID:
                if not perEffectMap_baseTypeID_typeID[baseTypeID][1]:
                    affectedItemsFromCurrentBaseType = perEffectMap_baseTypeID_typeID[baseTypeID][0]
                    affectedAndDecribed = len(affectedItemsFromCurrentBaseType.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrentBaseType.difference(perEffect_describedTypes))
                    total = len(globalMap_baseTypeID_typeID[baseTypeID])
                    baseTypeScore[baseTypeID] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected)
                    if debugLevel >= 1 and not stopDebugPrints:
                        cursor.execute(queryTypeName, (baseTypeID,))
                        for row in cursor: baseTypeName = row[0]
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Base item: {0}: {1}/{2} ({3:.3}%, inner score: {4:.3})".format(baseTypeName, affectedAndUndescribed, total, coverage, baseTypeScore[baseTypeID]))
                        if debugLevel == 2: print("Base item: {0}: {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(baseTypeName, affectedAndUndescribed, affectedAndDecribed, total, coverage, baseTypeScore[baseTypeID]))
            baseTypeOuterScore = calcOuterScore(baseTypeScore, perEffect_totalAffected, baseTypeWeight)
            #Print outer data
            if debugLevel >= 1 and not stopDebugPrints: print("Base item outer score: {0:.3}".format(baseTypeOuterScore))

            marketGroupWithVarsScore = {}
            marketGroupWithVarsWeight = 0.7
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
                            cursorParentMarket.execute(queryParentMarketGroup, (prependParentID,))
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
            typeNameCombinationWeight = 1.0
            for typeNameCombination in perEffectMap_typeNameCombination_typeID:
                if not perEffectMap_typeNameCombination_typeID[typeNameCombination][1]:
                    affectedItemsFromCurrenttypeNameCombination = perEffectMap_typeNameCombination_typeID[typeNameCombination][0]
                    affectedAndDecribed = len(affectedItemsFromCurrenttypeNameCombination.intersection(perEffect_describedTypes))
                    affectedAndUndescribed =  len(affectedItemsFromCurrenttypeNameCombination.difference(perEffect_describedTypes))
                    total = len(globalMap_typeNameCombination_typeID[typeNameCombination])
                    #typeNames are special: wee also need to consider how certain
                    #word combination covers full typeName. We start from zero
                    averageCoverage = 0
                    itemsNamedLikeThis = perEffectMap_typeNameCombination_typeID[typeNameCombination][0]
                    for typeID in itemsNamedLikeThis:
                        #Add number of words in combination divided by total number of words from any given item
                        averageCoverage += len(typeNameCombination)/globalMap_typeID_typeNameCombination[typeID][1]
                    #Then divide by number of items we checked, making it real average
                    averageCoverage = averageCoverage/len(itemsNamedLikeThis)
                    #Pass average coverage as additional balancing factor
                    typeNameCombinationScore[typeNameCombination] = calcInnerScore(affectedAndDecribed, affectedAndUndescribed, total, perEffect_totalAffected, 0.2 + averageCoverage*0.8)
                    if debugLevel >= 1 and not stopDebugPrints:
                        typeNameCombinationPrintable = " ".join(typeNameCombination)
                        coverage = (affectedAndDecribed + affectedAndUndescribed)/total * 100
                        if debugLevel == 1: print("Type name combination: \"{0}\": {1}/{2} ({3:.3}%, inner score: {4:.3})".format(typeNameCombinationPrintable, affectedAndUndescribed, total, coverage, typeNameCombinationScore[typeNameCombination]))
                        if debugLevel == 2: print("Type name combination: \"{0}\": {1}+{2}/{3} ({4:.3}%, inner score: {5:.3})".format(typeNameCombinationPrintable, affectedAndUndescribed, affectedAndDecribed, total, coverage, typeNameCombinationScore[typeNameCombination]))
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
            if maxOuterScore > 0.5:
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
                    perEffect_describedTypes |= globalMap_typeNameCombination_typeID[typeNameCombinationWinner]
                    perEffectMap_typeNameCombination_typeID[typeNameCombinationWinner][1] = True
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

        #These lists will contain IDs and more human-friendly names in tuples
        types = []
        groups = []
        categories = []
        baseTypes = []
        marketGroupsWithVars = []
        typeNameCombinations = []

        #Processing order matters here, as we're prepending comment lines to file
        #category > group > name > marketGroup > baseType > single items
        #Go through all items in list
        for typeID in singleItems:
            cursor.execute(queryTypeName, (typeID,))
            for row in cursor: typeName = row[0]
            #Make tuples and append them
            types.append((typeID, typeName))
        #As we're prepending lines, sort items by name in reverse order
        for type in sorted(types, key=lambda tuple: tuple[1], reverse=True):
            cursor.execute(queryGroupCategory, (globalMap_typeID_groupID[type[0]],))
            for row in cursor: categoryID = row[0]
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            #Prepend line with all the data we need
            effectLines.insert(0,"#Item: {0} [{1}]".format(type[1], categoryName))

        for baseTypeID in describedByBaseType:
            cursor.execute(queryTypeName, (baseTypeID,))
            for row in cursor: baseTypeName = row[0]
            baseTypes.append((baseTypeID, baseTypeName))
        for baseType in sorted(baseTypes, key=lambda tuple: tuple[1], reverse=True):
            cursor.execute(queryGroupCategory, (globalMap_typeID_groupID[baseType[0]],))
            for row in cursor: categoryID = row[0]
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            effectLines.insert(0,"#Variations of item: {0} ({1} of {2}) [{3}]".format(baseType[1], len(perEffectMap_baseTypeID_typeID[baseType[0]][0]), len(globalMap_baseTypeID_typeID[baseType[0]]), categoryName))

        for marketGroupID in describedByMarketGroupWithVars:
            cursor.execute(queryMarketGroupName, (marketGroupID,))
            for row in cursor: marketGroupName = row[0]
            #Prepend market group name with its parents names
            prependParentID = marketGroupID
            #Limit depth to avoid looping, as usual
            for depth in range(20):
                cursorParentMarket = db.cursor()
                cursorParentMarket.execute(queryParentMarketGroup, (prependParentID,))
                for row in cursorParentMarket:
                    prependParentID = row[0]
                if prependParentID:
                    cursor.execute(queryMarketGroupName, (prependParentID,))
                    for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                else: break
            marketGroupsWithVars.append((marketGroupID, marketGroupName))
        for marketGroup in sorted(marketGroupsWithVars, key=lambda tuple: tuple[1], reverse=True):
            effectLines.insert(0,"#Items from market group: {0} ({1} of {2})".format(marketGroup[1], len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroup[0]][0]), len(globalMap_marketGroupID_typeIDWithVariations[marketGroup[0]])))

        for typeNameCombination in describedByTypeNameCombination:
            typeNameCombinationPrint = " ".join(typeNameCombination)
            typeNameCombinations.append((typeNameCombination, typeNameCombinationPrint))
        for typeNameCombination in sorted(typeNameCombinations, key=lambda tuple: tuple[1], reverse=True):
            effectLines.insert(0,"#Items with name like: {0} ({1} of {2})".format(typeNameCombination[1], len(perEffectMap_typeNameCombination_typeID[typeNameCombination[0]][0]), len(globalMap_typeNameCombination_typeID[typeNameCombination[0]])))

        for groupID in describedByGroup:
            cursor.execute(queryGroupName, (groupID,))
            for row in cursor: groupName = row[0]
            groups.append((groupID, groupName))
        for group in sorted(groups, key=lambda tuple: tuple[1], reverse=True):
            cursor.execute(queryGroupCategory, (group[0],))
            for row in cursor: categoryID = row[0]
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            effectLines.insert(0,"#Items from group: {0} ({1} of {2}) [{3}]".format(group[1], len(perEffectMap_groupID_typeID[group[0]][0]), len(globalMap_groupID_typeID[group[0]]), categoryName))

        for categoryID in describedByCategory:
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            categories.append((categoryID, categoryName))
        for category in sorted(categories, key=lambda tuple: tuple[1], reverse=True):
            effectLines.insert(0,"#Items from category: {0} ({1} of {2})".format(category[1], len(perEffectMap_categoryID_typeID[category[0]][0]), len(globalMap_categoryID_typeID[category[0]])))

        #Combine all lines into single string
        effectContentsProcessed = "\n".join(effectLines)
        #If we're not debugging and contents actually changed - write changes to the file
        if debugLevel == 0 and (effectContentsProcessed != effectContentsSource):
            effectFile = open(os.path.join(effectsPath, effectFileName), 'w')
            effectFile.write(effectContentsProcessed)
            effectFile.close()
