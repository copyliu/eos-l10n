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
import sys
sys.path.append("..")

import sqlite3
import os.path
import re
import math
import copy

db = sqlite3.connect(os.path.expanduser(os.path.join("~", ".pyfa","eve.db")))

#List of queries
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
cursor = db.cursor()
cursor.execute(queryAllEffects)
for row in cursor:
    globalMap_effectNamePyfa_effectNameDB[re.sub(stripSpec, "", row[1])] = row[0]

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

#BaseType
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

#MarketGroup
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
# { [typeName] : set(typeID) }
#globalMap_typeName_typeID =  {}
# { typeID : set(typeName) }
#globalMap_typeID_typeName =  {}
#cursor.execute(queryPublishedTypeNames)
#for row in cursor:
    #typeID, typeName = row[0], row[1]
    #print typeName.split(" ")

def calcInnerScore(innerScore_affectedDescribed, innerScore_affectedUndescribed, innerScore_total, perEffect_totalAffected, weight):
    innerAffectedPortionDescribed = float(innerScore_affectedDescribed)/float(innerScore_total)
    innerAffectedPortionUndescribed = float(innerScore_affectedUndescribed)/float(innerScore_total)
    innerPortionTotal = innerAffectedPortionDescribed + innerAffectedPortionUndescribed
    innerScore = (innerAffectedPortionUndescribed + innerAffectedPortionDescribed/50)*(innerScore_affectedDescribed+innerScore_affectedUndescribed-1)
    return innerScore, innerPortionTotal

def calcOuterScore(innerScoreDict, perEffect_totalAffected, weight):
    #outerAffected = float(len(innerScoreDict))
    #if outerAffected: outerScore = math.fsum(innerScoreDict.itervalues())/(math.pow(outerAffected,0.5))
    #else: outerScore = 0.0
    #return outerScore
    #Return just max of the inner scores, including weight factor
    if float(len(innerScoreDict)):
        return innerScoreDict[max(innerScoreDict, key = lambda a: innerScoreDict.get(a))] * weight
    else: return 0.0

#Go through effect files one-by-one
effectsPath = os.path.join("..", "effects")
for effectFileName in os.listdir(effectsPath):
#Pick only effects we need for debugging purposes
#effectsToTest = ["modifyActiveShieldResonanceAndNullifyPassiveResonance.py", "customEffects.py"]
#for effectFileName in effectsToTest:
    basename, extension = effectFileName.split('.')
    #Ignore non-py files and exclude pyfa-specific 'effects'
    if extension == "py" and not basename in ("__init__", "customEffects"):
        #Gather all necessary data regarding items using this effect in single dictionary
        perEffectList_usedByTypes = set()
        cursorTypes = db.cursor()
        cursorTypes.execute(queryTypesUsedByEffect, (globalMap_effectNamePyfa_effectNameDB[basename],))
        for rowTypes in cursorTypes:
            typeID = rowTypes[0]
            perEffectList_usedByTypes.add(typeID)

        #Compose per-group map of items which are affected by current effect
        # { groupID : set(typeID) }
        perEffectMap_groupID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            groupID = globalMap_typeID_groupID[typeID]
            if not groupID in perEffectMap_groupID_typeID: perEffectMap_groupID_typeID[groupID] = set()
            perEffectMap_groupID_typeID[groupID].add(typeID)

        #Now, per-category map of items
        # { categoryID : set(typeID) }
        perEffectMap_categoryID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            categoryID = globalMap_typeID_categoryID[typeID]
            if not categoryID in perEffectMap_categoryID_typeID: perEffectMap_categoryID_typeID[categoryID] = set()
            perEffectMap_categoryID_typeID[categoryID].add(typeID)

        #Per-baseType map of variations
        # { baseTypeID : set(typeID) }
        perEffectMap_baseTypeID_typeID = {}
        for typeID in perEffectList_usedByTypes:
            baseTypeID = globalMap_typeID_baseTypeID[typeID]
            if not baseTypeID in perEffectMap_baseTypeID_typeID: perEffectMap_baseTypeID_typeID[baseTypeID] = set()
            perEffectMap_baseTypeID_typeID[baseTypeID].add(typeID)

        #Per-marketGroup map with variations
        # { marketGroupID : set(typeIDWithVariations) }
        perEffectMap_marketGroupID_typeIDWithVariations = {}
        for typeID in perEffectList_usedByTypes:
            if typeID in globalMap_typeID_marketGroupID: marketGroupIDs = globalMap_typeID_marketGroupID[typeID]
            else: marketGroupIDs = set()
            for marketGroupID in marketGroupIDs:
                if not marketGroupID in perEffectMap_marketGroupID_typeIDWithVariations: perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID] = set()
                perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID].add(typeID)

        #These dictionaries will store number of items in certain groups affected by
        #current effect for printing purposes
        # { groupID : int }
        perEffectMap_groupID_typesAffected = {}
        for groupID in perEffectMap_groupID_typeID:
            perEffectMap_groupID_typesAffected[groupID] = len(perEffectMap_groupID_typeID[groupID])
        # { categoryID : int }
        perEffectMap_categoryID_typesAffected = {}
        for categoryID in perEffectMap_categoryID_typeID:
            perEffectMap_categoryID_typesAffected[categoryID] = len(perEffectMap_categoryID_typeID[categoryID])
        # { baseTypeID : int }
        perEffectMap_baseTypeID_typesAffected = {}
        for baseTypeID in perEffectMap_baseTypeID_typeID:
            perEffectMap_baseTypeID_typesAffected[baseTypeID] = len(perEffectMap_baseTypeID_typeID[baseTypeID])
        # { marketGroupID : int }
        perEffectMap_marketGroupID_typesWithVariationsAffected = {}
        for marketGroupID in perEffectMap_marketGroupID_typeIDWithVariations:
            perEffectMap_marketGroupID_typesWithVariationsAffected[marketGroupID] = len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID])

        perEffect_totalAffected = len(perEffectList_usedByTypes)

        #show debug prints?
        printStuff = False
        if printStuff:
            print("\nEffect:", basename)
            print("Total items affected: {0}".format(perEffect_totalAffected))

        perEffect_describedTypes = set()
        describedByGroup = []
        describedByCategory = []
        describedByBaseType = []
        describedByMarketGroupWithVars = []

        iterate = True
        while iterate:
            groupScore = {}
            groupWeight = 1.0
            for groupID in perEffectMap_groupID_typeID:
                innerScore_affectedDescribed = len(perEffectMap_groupID_typeID[groupID].intersection(perEffect_describedTypes))
                innerScore_affectedUndescribed =  len(perEffectMap_groupID_typeID[groupID].difference(perEffect_describedTypes))
                innerScore_total = len(globalMap_groupID_typeID[groupID])
                groupScore[groupID], innerAffectedPortion = calcInnerScore(innerScore_affectedDescribed, innerScore_affectedUndescribed, innerScore_total, perEffect_totalAffected, groupWeight)
                if printStuff:
                    #Get data for print
                    cursor.execute(queryGroupName, (groupID,))
                    for row in cursor: groupName = row[0]
                    #Print inner data
                    print("Group: {0}: {1}+{2}/{3} ({4:.3}%, score: {5:.3})".format(groupName, innerScore_affectedUndescribed, innerScore_affectedDescribed, innerScore_total, innerAffectedPortion*100, groupScore[groupID]))
            groupOuterScore = calcOuterScore(groupScore, perEffect_totalAffected, groupWeight)
            #Print outer data
            if printStuff: print("Groups total score: {0:.3}".format(groupOuterScore))

            categoryScore = {}
            categoryWeight = 1.0
            for categoryID in perEffectMap_categoryID_typeID:
                innerScore_affectedDescribed = len(perEffectMap_categoryID_typeID[categoryID].intersection(perEffect_describedTypes))
                innerScore_affectedUndescribed =  len(perEffectMap_categoryID_typeID[categoryID].difference(perEffect_describedTypes))
                innerScore_total = len(globalMap_categoryID_typeID[categoryID])
                categoryScore[categoryID], innerAffectedPortion = calcInnerScore(innerScore_affectedDescribed, innerScore_affectedUndescribed, innerScore_total, perEffect_totalAffected, categoryWeight)
                if printStuff:
                    #Get data for print
                    cursor.execute(queryCategoryName, (categoryID,))
                    for row in cursor: categoryName = row[0]
                    #Print inner data
                    print("Category: {0}: {1}+{2}/{3} ({4:.3}%, score: {5:.3})".format(categoryName, innerScore_affectedUndescribed, innerScore_affectedDescribed, innerScore_total, innerAffectedPortion*100, categoryScore[categoryID]))
            categoryOuterScore = calcOuterScore(categoryScore, perEffect_totalAffected, categoryWeight)
            #Print outer data
            if printStuff: print("Category total score: {0:.3}".format(categoryOuterScore))

            baseTypeScore = {}
            baseTypeWeight = 1.0
            for baseTypeID in perEffectMap_baseTypeID_typeID:
                innerScore_affectedDescribed = len(perEffectMap_baseTypeID_typeID[baseTypeID].intersection(perEffect_describedTypes))
                innerScore_affectedUndescribed =  len(perEffectMap_baseTypeID_typeID[baseTypeID].difference(perEffect_describedTypes))
                innerScore_total = len(globalMap_baseTypeID_typeID[baseTypeID])
                baseTypeScore[baseTypeID], innerAffectedPortion = calcInnerScore(innerScore_affectedDescribed, innerScore_affectedUndescribed, innerScore_total, perEffect_totalAffected, baseTypeWeight)
                if printStuff:
                #Get data for print
                    cursor.execute(queryTypeName, (baseTypeID,))
                    for row in cursor: baseTypeName = row[0]
                    #Print inner data
                    print("Base item: {0}: {1}+{2}/{3} ({4:.3}%, score: {5:.3})".format(baseTypeName, innerScore_affectedUndescribed, innerScore_affectedDescribed, innerScore_total, innerAffectedPortion*100, baseTypeScore[baseTypeID]))
            baseTypeOuterScore = calcOuterScore(baseTypeScore, perEffect_totalAffected, baseTypeWeight)
            #Print outer data
            if printStuff: print("Base item total score: {0:.3}".format(baseTypeOuterScore))

            marketGroupWithVarsScore = {}
            marketGroupWithVarsWeight = 0.7
            for marketGroupID in perEffectMap_marketGroupID_typeIDWithVariations:
                innerScore_affectedDescribed = len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID].intersection(perEffect_describedTypes))
                innerScore_affectedUndescribed =  len(perEffectMap_marketGroupID_typeIDWithVariations[marketGroupID].difference(perEffect_describedTypes))
                innerScore_total = len(globalMap_marketGroupID_typeIDWithVariations[marketGroupID])
                marketGroupWithVarsScore[marketGroupID], innerAffectedPortion = calcInnerScore(innerScore_affectedDescribed, innerScore_affectedUndescribed, innerScore_total, perEffect_totalAffected, marketGroupWithVarsWeight)
                if printStuff:
                    #Get data for print
                    cursor.execute(queryMarketGroupName, (marketGroupID,))
                    for row in cursor: marketGroupName = row[0]
                    #Prepend market group name with its parents names
                    prependParentID = marketGroupID
                    for depth in range(20):
                        cursorParentMarket = db.cursor()
                        cursorParentMarket.execute(queryParentMarketGroup, (prependParentID,))
                        for row in cursorParentMarket:
                            prependParentID = row[0]
                        if prependParentID:
                            cursor.execute(queryMarketGroupName, (prependParentID,))
                            for row in cursor: marketGroupName = "{0} > {1}".format(row[0], marketGroupName)
                        else: break
                    #Print inner data
                    print("Market group with variations: {0}: {1}+{2}/{3} ({4:.3}%, score: {5:.3})".format(marketGroupName, innerScore_affectedUndescribed, innerScore_affectedDescribed, innerScore_total, innerAffectedPortion*100, marketGroupWithVarsScore[marketGroupID]))
            marketGroupWithVarsOuterScore = calcOuterScore(marketGroupWithVarsScore, perEffect_totalAffected, marketGroupWithVarsWeight)
            #Print outer data
            if printStuff: print("Market group total score: {0:.3}".format(marketGroupWithVarsOuterScore))

            printStuff = False
            #print "---"

            maxOuterScore = max(groupOuterScore, categoryOuterScore, baseTypeOuterScore, marketGroupWithVarsOuterScore)
            if maxOuterScore > 0.5:
                if maxOuterScore == groupOuterScore:
                    groupWinner = max(groupScore, key=groupScore.get)
                    describedByGroup.append(groupWinner)
                    #add all items described by winning group into set of described items
                    perEffect_describedTypes |= globalMap_groupID_typeID[groupWinner]
                    del perEffectMap_groupID_typeID[groupWinner]
                elif maxOuterScore == categoryOuterScore:
                    categoryWinner = max(categoryScore, key=categoryScore.get)
                    describedByCategory.append(categoryWinner)
                    perEffect_describedTypes |= globalMap_categoryID_typeID[categoryWinner]
                    del perEffectMap_categoryID_typeID[categoryWinner]
                elif maxOuterScore == baseTypeOuterScore:
                    baseTypeWinner = max(baseTypeScore, key=baseTypeScore.get)
                    describedByBaseType.append(baseTypeWinner)
                    perEffect_describedTypes |= globalMap_baseTypeID_typeID[baseTypeWinner]
                    del perEffectMap_baseTypeID_typeID[baseTypeWinner]
                elif maxOuterScore == marketGroupWithVarsOuterScore:
                    marketGroupWithVarsWinner = max(marketGroupWithVarsScore, key=marketGroupWithVarsScore.get)
                    describedByMarketGroupWithVars.append(marketGroupWithVarsWinner)
                    perEffect_describedTypes |= globalMap_marketGroupID_typeIDWithVariations[marketGroupWithVarsWinner]
                    del perEffectMap_marketGroupID_typeIDWithVariations[marketGroupWithVarsWinner]
            #Stop if we have score less than some critical value, all undescribed
            #items will be provided as plain list
            else: iterate = False
            #Also stop if we described all items
            if perEffectList_usedByTypes.issubset(perEffect_describedTypes): iterate = False
        #print "Single items:", set(perEffectList_usedByTypes).difference(perEffect_describedTypes)
        #print "Groups:", describedByGroup
        #print "Categories:", describedByCategory
        #print "Base item:", describedByBaseType
        #print "Market group with variations:", describedByMarketGroupWithVars

        #Print stuff to effect file
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

        types = []
        groups = []
        categories = []
        baseTypes = []
        marketGroupsWithVars = []

        for typeID in set(perEffectList_usedByTypes).difference(perEffect_describedTypes):
            cursor.execute(queryTypeName, (typeID,))
            for row in cursor: typeName = row[0]
            types.append((typeID, typeName))
        for type in sorted(types, key=lambda tuple: tuple[1], reverse=True):
            cursor.execute(queryGroupCategory, (globalMap_typeID_groupID[type[0]],))
            for row in cursor: categoryID = row[0]
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
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
            effectLines.insert(0,"#Variations of item: {0} ({1} of {2}) [{3}]".format(baseType[1], perEffectMap_baseTypeID_typesAffected[baseType[0]], len(globalMap_baseTypeID_typeID[baseType[0]]), categoryName))

        for marketGroupID in describedByMarketGroupWithVars:
            #Get data for print
            cursor.execute(queryMarketGroupName, (marketGroupID,))
            for row in cursor: marketGroupName = row[0]
            #Prepend market group name with its parents names
            prependParentID = marketGroupID
            #Limit depth
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
            effectLines.insert(0,"#Items from market group: {0} ({1} of {2})".format(marketGroup[1], perEffectMap_marketGroupID_typesWithVariationsAffected[marketGroup[0]], len(globalMap_marketGroupID_typeIDWithVariations[marketGroup[0]])))

        for groupID in describedByGroup:
            cursor.execute(queryGroupName, (groupID,))
            for row in cursor: groupName = row[0]
            groups.append((groupID, groupName))
        for group in sorted(groups, key=lambda tuple: tuple[1], reverse=True):
            cursor.execute(queryGroupCategory, (group[0],))
            for row in cursor: categoryID = row[0]
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            effectLines.insert(0,"#Items from group: {0} ({1} of {2}) [{3}]".format(group[1], perEffectMap_groupID_typesAffected[group[0]], len(globalMap_groupID_typeID[group[0]]), categoryName))

        for categoryID in describedByCategory:
            cursor.execute(queryCategoryName, (categoryID,))
            for row in cursor: categoryName = row[0]
            categories.append((categoryID, categoryName))
        for category in sorted(categories, key=lambda tuple: tuple[1], reverse=True):
            effectLines.insert(0,"#Items from category: {0} ({1} of {2})".format(category[1], perEffectMap_categoryID_typesAffected[category[0]], len(globalMap_categoryID_typeID[category[0]])))

        effectContentsProcessed = "\n".join(effectLines)
        if effectContentsProcessed != effectContentsSource:
            effectFile = open(os.path.join(effectsPath, effectFileName), 'w')
            effectFile.write(effectContentsProcessed)
            effectFile.close()
