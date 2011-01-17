#!/usr/bin/env python3
#===============================================================================
# Copyright (C) 2010 Anton Vorobyov
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================


'''
This script is used to compare two different database versions.
It shows removed/changed/new items with list of changed effects,
changed attributes and effects which were renamed
'''
from optparse import OptionParser
import sqlite3
import os.path
import re

usage = "usage: %prog [--old=OLD] --new=NEW [-ear]"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--old", help="path to old cache data dump (if none specified default pyfa path to database is taken)", type="string", default=os.path.join("~", ".pyfa","eve.db"))
parser.add_option("-n", "--new", help="path to new cache data dump", type="string")
parser.add_option("-e", "--noeffects", action="store_false", dest="effects", help="don't show list of changed effects", default=True)
parser.add_option("-a", "--noattributes", action="store_false", dest="attributes", help="don't show list of changed attributes", default=True)
parser.add_option("-r", "--norenames", action="store_false", dest="renames", help="don't show list of renamed data", default=True)
(options, args) = parser.parse_args()

#fetch database names from command line arguments
if options.old is not None and options.new is not None:
    oldDB = sqlite3.connect(os.path.expanduser(options.old))
    newDB = sqlite3.connect(os.path.expanduser(options.new))
else:
    import sys

    sys.stderr.write("You need to specify at least 1 database file. Run script with --help option for further info.\n")
    sys.exit()

#We don't rely on pyfa backend for overrides, setting them manually
overrides = '''
UPDATE invtypes SET published = '1' WHERE typeName = 'Freki';
UPDATE invtypes SET published = '1' WHERE typeName = 'Mimir';
UPDATE invtypes SET published = '1' WHERE typeName = 'Utu';
UPDATE invtypes SET published = '1' WHERE typeName = 'Adrestia';
'''
for statement in overrides.split(";\n"):
    oldCursor = oldDB.cursor()
    oldCursor.execute(statement)
    newCursor = newDB.cursor()
    newCursor.execute(statement)

#initialization of few things used by both changed/renamed effects list
if options.effects or options.renames:
    effectsPath = os.path.join("..", "effects")
    implemented = []

    for filename in os.listdir(effectsPath):
        basename, extension = filename.rsplit('.', 1)
        #Ignore non-py files and exclude implementation-specific 'effect'
        if extension == "py" and extension not in ("__init__"):
            implemented.append(basename)

    #effects' names are used w/o any special symbols by eos
    stripSpec = "[^A-Za-z0-9]"

    #Method to get data if effect iss implemented in eos or not
    def getEffectStatus(effectName):
        pyfaName = re.sub(stripSpec, "", effectName)
        if pyfaName in implemented: return 'y'
        else: return 'n'

if options.effects or options.attributes:
    #format:
    #key: item id
    #value: [set(effect id 1, effect id 2, ...), {[key: attribute id] | value}]
    oldDict = {}
    newDict = {}

    for database, dictionary in ((oldDB, oldDict), (newDB, newDict)):
        if options.effects:
            #Compose list of item IDs (row[0]) and attach list of effect IDs (row[1]) to each
            query = 'SELECT invtypes.typeID, dgmeffects.effectID FROM invtypes INNER JOIN dgmtypeeffects ON dgmtypeeffects.typeID = invtypes.typeID INNER JOIN dgmeffects ON dgmeffects.effectID = dgmtypeeffects.effectID WHERE invtypes.published = 1'
            c = database.cursor()
            c.execute(query)
            for row in c:
                #if there's no such item in dictionary, initialize empty parent list
                if not row[0] in dictionary: dictionary[row[0]] = [set(), {}]
                #add effect to the set
                effectSet = dictionary[row[0]][0]
                effectSet.add(row[1])
        if options.attributes:
            #If there's no list of items, create it and add base and additional attributes to it
            query = 'SELECT dgmtypeattribs.typeID, dgmtypeattribs.attributeID, dgmtypeattribs.value, invtypes.mass, invtypes.capacity, invtypes.volume FROM dgmtypeattribs INNER JOIN invtypes ON dgmtypeattribs.typeID = invtypes.typeID INNER JOIN invgroups ON invtypes.groupID = invgroups.groupID INNER JOIN invcategories ON invgroups.categoryID = invcategories.categoryID WHERE invtypes.published = 1 AND (invcategories.categoryName = "Ship" OR invcategories.categoryName = "Module" OR invcategories.categoryName = "Charge" OR invcategories.categoryName = "Skill" OR invcategories.categoryName = "Drone" OR invcategories.categoryName = "Implant" OR invcategories.categoryName = "Subsystem" OR invcategories.categoryName = "Celestial")'
            c = database.cursor()
            c.execute(query)
            for row in c:
                #if there's no such item in dictionary, initialize empty parent list
                if not row[0] in dictionary: dictionary[row[0]] = [set(), {}]
                attrDict = dictionary[row[0]][1]
                #add base attributes: mass (4), capacity (38) and volume (161)
                attrDict[4] = row[3]
                attrDict[38] = row[4]
                attrDict[161] = row[5]
                #add non-base attributes to the dictionary
                if not row[1] in (4, 38, 161): attrDict[row[1]] = row[2]
                else: print("Warning: base attribute is described in non-base attribute table")

    #Lists contain IDs of items which have the same/changed set of effects' IDs
    same = []
    changed = []

    #iterates through item IDs from old database
    for itemId in oldDict:
        #check if there's such ID in new database
        if itemId in newDict:
            #assume that items are the same, try to prove that it's wrong later
            isSame = True
            oldEffectSet = oldDict[itemId][0]
            newEffectSet = newDict[itemId][0]
            #if item with the same ID and the same set of effects - move to following tests
            if oldEffectSet == newEffectSet:
                oldAttrDict = oldDict[itemId][1]
                newAttrDict = newDict[itemId][1]
                #if set of attributes does not coincide - perform further checks
                if oldAttrDict != newAttrDict:
                    #cycle through attribute list of old items
                    for attributeId in oldAttrDict:
                        #it should be present in new item
                        if attributeId in newAttrDict:
                            oldVal = oldAttrDict[attributeId]
                            newVal = newAttrDict[attributeId]
                            #eve considers none and zero values as zero
                            for val in (oldVal, newVal):
                                if val is None: val = 0
                                if int(val) == val: val = int(val)
                            if (oldVal or newVal) and oldVal != newVal:
                                isSame = False
                                break
                        #if there's no such attribute in new item - it's not the same
                        else: isSame = False
                    #if some attribute is present in new item but absent in old, it's not the same
                    for attributeId in newAttrDict:
                        if not attributeId in oldAttrDict:
                            isSame = False
                            break
            #if effects set is not the same - items are not the same
            else: isSame = False
            if isSame: same.append(itemId)
            else: changed.append(itemId)

    #Delete same items from both dictionaries
    for itemId in same:
        del oldDict[itemId], newDict[itemId]

#As pyfa uses names as unique ID, we have to keep track of changed
if options.renames:
    def findRenames(renamedList, query, strip = False):
        oldRenDict = {}
        newRenDict = {}

        for database, dictionary in ((oldDB, oldRenDict), (newDB, newRenDict)):
            c = database.cursor()
            c.execute(query)
            for row in c:
                if strip: dictionary[row[0]] = re.sub(stripSpec, "", row[1])
                else: dictionary[row[0]] = row[1]

        for someID in oldRenDict:
            if someID in newRenDict:
                if oldRenDict[someID] != newRenDict[someID]:
                    renamedList.append((oldRenDict[someID],newRenDict[someID]))

    renamedEffects = []
    query = 'SELECT effectID, effectName FROM dgmeffects'
    findRenames(renamedEffects, query, strip = True)

    renamedAttributes = []
    query = 'SELECT attributeID, attributeName FROM dgmattribs'
    findRenames(renamedAttributes, query)

    renamedCategories = []
    query = 'SELECT categoryID, categoryName FROM invcategories'
    findRenames(renamedCategories, query)

    renamedGroups = []
    query = 'SELECT groupID, groupName FROM invgroups'
    findRenames(renamedGroups, query)

    renamedMarketGroups = []
    query = 'SELECT marketGroupID, marketGroupName FROM invmarketgroups'
    findRenames(renamedMarketGroups, query)

    renamedTypes = []
    query = 'SELECT typeID, typeName FROM invtypes'
    findRenames(renamedTypes, query)

#Print db versions
oldMeta = {}
newMeta = {}
query = 'SELECT fieldName, fieldValue FROM metadata'
c = oldDB.cursor()
c.execute(query)
for row in c:
    oldMeta[row[0]] = row[1]
c = newDB.cursor()
c.execute(query)
for row in c:
    newMeta[row[0]] = row[1]

#Print jobs
print("Comparing databases:\n{0}-{1}\n{2}-{3}\n".format(oldMeta["version"], oldMeta["release"], newMeta["version"], newMeta["release"]))
if options.effects or options.attributes:
    #print legend only when there're any interesting changes
    if changed:
        print('[+] - new item\n[-] - removed item\n[*] - changed item\n  [+] - effect or attribute has been added to item\n  [-] - effect or attribute has been removed from item\n  [y] - effect is implemented\n  [n] - effect is not implemented\n\nItems:')

        #queries to get item and effect names
        queryTypeName = 'SELECT invtypes.typeName FROM invtypes WHERE invtypes.typeID = ?'
        if options.effects: queryEffectName = 'SELECT dgmeffects.effectName FROM dgmeffects WHERE dgmeffects.effectID = ?'
        if options.attributes: queryAttributeName = 'SELECT dgmattribs.attributeName FROM dgmattribs WHERE dgmattribs.attributeID = ?'

        #process added/removed items; only effect list is printed for ease of maintenance,
        #attributes are not shown as there're usually too many of them
        def printAbsentItems(dict, db, sign):
            for itemId in dict:
                #items which are not changed but remain in old/new list were removed/added
                if not itemId in changed:
                    c = db.cursor()
                    c.execute(queryTypeName, (itemId,))
                    #print item name with added/deleted tag
                    for row in c:
                        print("\n[{0}] {1}".format(sign, row[0]))
                    if options.effects:
                        #print effects list
                        for effect in dict[itemId][0]:
                            c = db.cursor()
                            c.execute(queryEffectName, (effect,))
                            for row in c:
                                print("  [{0}|{1}] {2}".format(sign, getEffectStatus(row[0]), re.sub(stripSpec, "",row[0])))

        if options.effects:
            #print old items
            printAbsentItems(oldDict, oldDB, "-")

        #process changed items
        for itemId in changed:
            c = newDB.cursor()
            c.execute(queryTypeName, (itemId,))
            #print item name with changed tag
            for row in c:
                print("\n[*] {0}".format(row[0]))

            if options.effects:
                #print effects list
                for dict, compDict, db, sign in ((oldDict, newDict, oldDB, "-"), (newDict, oldDict, newDB, "+")):
                    for effect in dict[itemId][0]:
                        #we don't want to show effects which were unchanged
                        if not effect in compDict[itemId][0]:
                            c = db.cursor()
                            c.execute(queryEffectName, (effect,))
                            for row in c:
                                print("  [{0}|{1}] {2}".format(sign, getEffectStatus(row[0]), re.sub(stripSpec, "",row[0])))

            if options.attributes:
                #prints attributes which are present in baseDict but absent in compDict
                def printAbsentAttrs(baseDict, compDict, db, tag):
                    for attributeId in baseDict:
                        if not attributeId in compDict:
                            value = baseDict[attributeId]
                            if not value: value = 0
                            c = db.cursor()
                            c.execute(queryAttributeName, (attributeId,))
                            for row in c:
                                #print zeros instead of none as eve considers none values this way
                                print("  [{0}] {1}: {2}".format(tag, row[0], value or 0))

                oldAttrDict = oldDict[itemId][1]
                newAttrDict = newDict[itemId][1]

                #seek for removed attributes
                printAbsentAttrs(oldAttrDict, newAttrDict, oldDB, "-")

                #print changed attributes
                for attributeId in oldAttrDict:
                    if attributeId in newAttrDict:
                        if oldAttrDict[attributeId] != newAttrDict[attributeId]:
                            oldVal = oldAttrDict[attributeId]
                            newVal = newAttrDict[attributeId]
                            if (oldVal or newVal) and oldVal != newVal:
                                #if attributes exist in both DBs use new one
                                c = newDB.cursor()
                                c.execute(queryAttributeName, (attributeId,))
                                for row in c:
                                    #print zeros instead of none as eve considers none values this way
                                    print("  [*] {0}: {1} => {2}".format(row[0], oldVal or 0, newVal or 0))

                #seek for added attributes
                printAbsentAttrs(newAttrDict, oldAttrDict, newDB, "+")

        if options.effects:
            #print new items
            printAbsentItems(newDict, newDB, "+")

if options.renames:
    def printRenames(renamedList, title, implementedEffectTag = False):
        if renamedList:
            print('\nRenamed ' + title + ':')
            for couple in renamedList:
                if implementedEffectTag: print("\n[{0}] \"{1}\"\n[{2}] \"{3}\"".format(getEffectStatus(couple[0]), couple[0], getEffectStatus(couple[1]), couple[1]))
                else: print("\n\"{0}\"\n\"{1}\"".format(couple[0], couple[1]))

    title = 'effects'
    printRenames(renamedEffects, title, implementedEffectTag = True)

    title = 'attributes'
    printRenames(renamedAttributes, title)

    title = 'categories'
    printRenames(renamedCategories, title)

    title = 'groups'
    printRenames(renamedGroups, title)

    title = 'market groups'
    printRenames(renamedMarketGroups, title)

    title = 'items'
    printRenames(renamedTypes, title)
