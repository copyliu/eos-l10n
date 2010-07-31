#!/usr/bin/env python2.6
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
This script pulls data out of EVE cache and makes an SQLite dump
Reverence library by Entity is used, check http://wiki.github.com/ntt/reverence/ for info
As reverence uses the same python version as EVE client (2.x series), script cannot be converted to python3
Example commands to run the script for default paths:
Tranquility: python2.6 eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_tranquility/cache" --dump="~/Desktop/eve.db"
Singularity: python2.6 eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE (Singularity)" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_(singularity)_singularity/cache" --sisi --dump="~/Desktop/evetest.db"
'''

schema = '''
CREATE TABLE "dgmattribs" (
  "attributeID" smallint(6) NOT NULL,
  "attributeName" varchar(100) default NULL,
  "attributeCategory" tinyint(3) default NULL,
  "description" varchar(1000) default NULL,
  "maxAttributeID" smallint(6) default NULL,
  "attributeIdx" smallint(6) default NULL,
  "graphicID" smallint(6) default NULL,
  "chargeRechargeTimeID" smallint(6) default NULL,
  "defaultValue" double default NULL,
  "published" tinyint(1) default NULL,
  "unitID" tinyint(3) default NULL,
  "displayName" varchar(100) default NULL,
  "stackable" tinyint(1) default NULL,
  "highIsGood" tinyint(1) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("attributeID")
);
CREATE INDEX "dgmattribs_IX_attributeCategory" ON "dgmattribs" ("attributeCategory");

CREATE TABLE "dgmeffects" (
  "effectID" smallint(6) NOT NULL,
  "effectName" varchar(400) default NULL,
  "effectCategory" smallint(6) default NULL,
  "preExpression" int(11) default NULL,
  "postExpression" int(11) default NULL,
  "description" varchar(1000) default NULL,
  "guid" varchar(60) default NULL,
  "graphicID" smallint(6) default NULL,
  "isOffensive" tinyint(1) default NULL,
  "isAssistance" tinyint(1) default NULL,
  "durationAttributeID" smallint(6) default NULL,
  "trackingSpeedAttributeID" smallint(6) default NULL,
  "dischargeAttributeID" smallint(6) default NULL,
  "rangeAttributeID" smallint(6) default NULL,
  "falloffAttributeID" smallint(6) default NULL,
  "published" tinyint(1) default NULL,
  "displayName" varchar(100) default NULL,
  "isWarpSafe" tinyint(1) default NULL,
  "rangeChance" tinyint(1) default NULL,
  "electronicChance" tinyint(1) default NULL,
  "propulsionChance" tinyint(1) default NULL,
  "distribution" tinyint(4) default NULL,
  "sfxName" varchar(20) default NULL,
  "npcUsageChanceAttributeID" smallint(6) default NULL,
  "npcActivationChanceAttributeID" smallint(6) default NULL,
  "fittingUsageChanceAttributeID" smallint(6) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("effectID")
);

CREATE TABLE "dgmtypeattribs" (
  "typeID" smallint(6) NOT NULL,
  "attributeID" smallint(6) NOT NULL,
  "value" double default NULL,
  PRIMARY KEY ("typeID","attributeID")
);
CREATE INDEX "dgmtypeattribs_IX_typeID" ON "dgmtypeattribs" ("typeID");
CREATE INDEX "dgmtypeattribs_IX_attributeID" ON "dgmtypeattribs" ("attributeID");

CREATE TABLE "dgmtypeeffects" (
  "typeID" smallint(6) NOT NULL,
  "effectID" smallint(6) NOT NULL,
  "isDefault" tinyint(1) default NULL,
  PRIMARY KEY ("typeID","effectID")
);
CREATE INDEX "dgmtypeeffects_IX_typeID" ON "dgmtypeeffects" ("typeID");
CREATE INDEX "dgmtypeeffects_IX_effectID" ON "dgmtypeeffects" ("effectID");

CREATE TABLE "icons" (
  "iconID" smallint(6) NOT NULL,
  "iconFile" varchar(10) NOT NULL,
  "description" varchar(100) NOT NULL,
  "obsolete" tinyint(1) NOT NULL,
  "iconType" smallint(6) NOT NULL,
  PRIMARY KEY ("iconID")
);

CREATE TABLE "invcategories" (
  "categoryID" tinyint(3) NOT NULL,
  "categoryName" varchar(100) default NULL,
  "description" varchar(3000) default NULL,
  "graphicID" smallint(6) default NULL,
  "published" tinyint(1) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("categoryID")
);
CREATE INDEX "invcategories_IX_categoryName" ON "invcategories" ("categoryName");

CREATE TABLE "invmarketgroups" (
  "parentGroupID" smallint(6) default NULL,
  "marketGroupID" smallint(6) NOT NULL,
  "marketGroupName" varchar(100) default NULL,
  "description" varchar(3000) default NULL,
  "graphicID" smallint(6) default NULL,
  "hasTypes" tinyint(1) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  "types" varchar(3000) default NULL,
  PRIMARY KEY ("marketGroupID")
);
CREATE INDEX "invmarketgroups_IX_parentGroupID" ON "invmarketgroups" ("parentGroupID");

CREATE TABLE "invmetagroups" (
  "metaGroupID" smallint(6) NOT NULL,
  "metaGroupName" varchar(100) default NULL,
  "description" varchar(1000) default NULL,
  "graphicID" smallint(6) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("metaGroupID")
);

CREATE TABLE "invmetatypes" (
  "typeID" smallint(6) NOT NULL,
  "parentTypeID" smallint(6) default NULL,
  "metaGroupID" smallint(6) default NULL,
  PRIMARY KEY ("typeID")
);
CREATE INDEX "invmetatypes_IX_parentTypeID" ON "invmetatypes" ("parentTypeID");

CREATE TABLE "invgroups" (
  "categoryID" tinyint(3) default NULL,
  "groupID" smallint(6) NOT NULL,
  "groupName" varchar(100) default NULL,
  "description" varchar(3000) default NULL,
  "graphicID" smallint(6) default NULL,
  "useBasePrice" tinyint(1) default NULL,
  "allowManufacture" tinyint(1) default NULL,
  "allowRecycler" tinyint(1) default NULL,
  "anchored" tinyint(1) default NULL,
  "anchorable" tinyint(1) default NULL,
  "fittableNonSingleton" tinyint(1) default NULL,
  "published" tinyint(1) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("groupID")
);
CREATE INDEX "invgroups_IX_categoryID" ON "invgroups" ("categoryID");

CREATE TABLE "invtypes" (
  "typeID" smallint(6) NOT NULL,
  "groupID" smallint(6) default NULL,
  "typeName" varchar(100) default NULL,
  "description" varchar(3000) default NULL,
  "graphicID" smallint(6) default NULL,
  "radius" double default NULL,
  "mass" double default NULL,
  "volume" double default NULL,
  "capacity" double default NULL,
  "portionSize" int(11) default NULL,
  "raceID" tinyint(3) default NULL,
  "basePrice" double default NULL,
  "published" tinyint(1) default NULL,
  "marketGroupID" smallint(6) default NULL,
  "chanceOfDuplicating" double default NULL,
  "soundID" smallint(6) default NULL,
  "categoryID" smallint(6) default NULL,
  "iconID" smallint(6) default NULL,
  "dataID" int(11) default NULL,
  PRIMARY KEY ("typeID")
);
CREATE INDEX "invtypes_IX_groupID" ON "invtypes" ("groupID");
CREATE INDEX "invtypes_IX_marketGroupID" ON "invtypes" ("marketGroupID");
'''

staticData = '''
CREATE TABLE "dgmAttributeCategories" (
  "categoryID" tinyint(3) NOT NULL,
  "categoryName" varchar(50) default NULL,
  "categoryDescription" varchar(200) default NULL,
  PRIMARY KEY ("categoryID")
);
'''

metadataTable = '''
CREATE TABLE "dumpmetadata" (
  "fieldName" varchar(50) NOT NULL,
  "fieldValue" varchar(100) default NULL,
  PRIMARY KEY ("fieldName")
);
'''

#{ source table name : dest table name }
tableMap = {
"allianceshortnames"            : None,
"billtypes"                     : None,
"certificaterelationships"      : None,
"certificates"                  : None,
"corptickernames"               : None,
"dgmattribs"                    : "dgmattribs",
"dgmeffects"                    : "dgmeffects",
"dgmtypeattribs"                : "dgmtypeattribs",
"dgmtypeeffects"                : "dgmtypeeffects",
"evegraphics"                   : None,
"evelocations"                  : None,
"eveowners"                     : None,
"eveunits"                      : None,
"groupsByCategories"            : None,
"icons"                         : "icons",
"invbptypes"                    : None,
"invcategories"                 : "invcategories",
"invcontrabandTypesByFaction"   : None,
"invcontrabandTypesByType"      : None,
"invgroups"                     : "invgroups",
"invmetagroups"                 : "invmetagroups",
"invmetatypes"                  : "invmetatypes",
"invmetatypesByTypeID"          : None,
"invreactiontypes"              : None,
"invtypes"                      : "invtypes",
"locationscenes"                : None,
"locationwormholeclasses"       : None,
"mapcelestialdescriptions"      : None,
"ownericons"                    : None,
"ramactivities"                 : None,
"ramaltypes"                    : None,
"ramaltypesdetailpercategory"   : None,
"ramaltypesdetailpergroup"      : None,
"ramcompletedstatuses"          : None,
"ramtypematerials"              : None,
"ramtyperequirements"           : None,
"schematics"                    : None,
"schematicsByPin"               : None,
"schematicsByType"              : None,
"schematicspinmap"              : None,
"schematicstypemap"             : None,
"shiptypes"                     : None,
"sounds"                        : None,
"typesByGroups"                 : None,
"typesByMarketGroups"           : None
}

def processTableValues(tableData):
    for row in tableData:
        for key in row.iterkeys():
            t = type(row[key])
            #text should be in singlequotes with singlequotes escaped by singlequotes
            if t in (str, unicode): row[key] = "'{0}'".format(row[key].replace("'", "''"))
            #bool values are used as tinyint(1) in database
            #also convert to string for proper operation of join
            elif t is bool: row[key] = str(int(row[key]))
            #lists are converted to csv
            elif t is list: row[key] = "'" + ",".join(map(str, row[key])) + "'"
            #pass empty strings to sql in  case of no data
            elif row[key] == None: row[key] = "''"
            #convert everything else to str for proper operation of join
            else: row[key] = str(row[key])
    return

def insertTableValues(tableData, tableName):
    for row in tableData:
        headers = []
        values = []
        for header in row.iterkeys():
            headers.append(header)
            values.append(row[header])
        query = "INSERT INTO {0} ({1}) VALUES({2})".format(tableName,",".join(headers),",".join(values))
        c.execute(query)
    return

def getSourceHeaders(sourceTable):
    sourceHeaders = None
    guid = getattr(sourceTable, "__guid__", "None")
    if guid == "util.IndexRowset":
        sourceHeaders = list(sourceTable.header)
    elif guid == "util.FilterRowset":
        sourceHeaders = list(sourceTable.header)
    elif guid == "util.IndexedRowLists":
        headerSet = set()
        for item in sourceTable.iterkeys():
            for row in sourceTable[item]:
                for headerName in row.__header__.Keys():
                    headerSet.add(headerName)
        sourceHeaders = list(headerSet)
    return sourceHeaders

def getDestHeaders(tableName):
    c.execute("PRAGMA table_info({0})".format(tableName))
    destHeaders = [row[1] for row in c]
    return destHeaders

def getCommonHeaders(sourceHeaders, destHeaders):
    headerList = []
    #fill header list with columns common for source and destination
    for sourceHeader in sourceHeaders:
        if sourceHeader in destHeaders:
            headerList.append(sourceHeader)
    return headerList

def printNonCommonHeaders(headerList, sourceHeaders, destHeaders, tableName):
    for sourceHeader in sourceHeaders:
        if not sourceHeader in headerList:
            print "Warning: data dump schema does not have column for", tableName + "." + sourceHeader
    for destHeader in destHeaders:
        if not destHeader in headerList:
            print "Warning: source does not contain data for", tableName + "." + destHeader
    return

def getTableData(sourceTable, tableName, headerList):
    dataRows = []
    guid = getattr(sourceTable, "__guid__", "None")
    if guid == "util.IndexRowset":
        for values in sourceTable.Select(*headerList):
            dataRow = {}
            if len(headerList) != len(values):
                print "Error: malformed data in source table", tableName
                return None
            for i in xrange(len(headerList)):
                dataRow[headerList[i]] = values[i]
            dataRows.append(dataRow)
    elif guid == "util.FilterRowset" or guid == "util.IndexedRowLists":
        for element in sourceTable.iterkeys():
            for row in sourceTable[element]:
                dataRow = {}
                for header in headerList:
                    value = getattr(row, header, None)
                    if value or value == 0 or value == 0.0: dataRow[header] = value
                dataRows.append(dataRow)
    return dataRows

def processTable(sourceTable, tableName):
    #get headers from source table
    sourceHeaders = getSourceHeaders(sourceTable)
    if not sourceHeaders:
        print "Error: unknown type for", tableName, "source table"
        return
    #get column names from database schema
    destHeaders = getDestHeaders(tableName)
    #get map of common headers
    headerList = getCommonHeaders(sourceHeaders, destHeaders)
    #inform if we have no proper destination for data or source for existing destination
    printNonCommonHeaders(headerList, sourceHeaders, destHeaders, tableName)
    #get data from source and process it
    tableData = getTableData(sourceTable, tableName, headerList)
    #modify data to satisfy SQL query requirements
    processTableValues(tableData)
    #insert everything into table
    insertTableValues(tableData, tableName)
    return

if __name__ == "__main__":
    from optparse import OptionParser
    from ConfigParser import ConfigParser
    from reverence import blue
    import sqlite3
    import re
    import os
    import sys
    #ugly trick to set encoding
    reload(sys)
    sys.setdefaultencoding("utf8")

    usage = "usage: %prog [--old=OLD] --new=NEW [-ear]"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--eve", help="path to eve folder")
    parser.add_option("-c", "--cache", help="path to eve cache folder")
    parser.add_option("-d", "--dump", help="where to data dump file for writing")
    parser.add_option("-r", "--release", help="database release number, defaults to 1", default="1")
    parser.add_option("-s", "--sisi", action="store_true", dest="singularity", help="if you're going to work with singulary test server data, use this option", default=False)
    (options, args) = parser.parse_args()

    if not options.eve or not options.cache or not options.dump:
        sys.stderr.write("You need to specify paths to eve folder, cache folder and dump file. Run script with --help option for further info.\n")
        sys.exit()

    if options.singularity: server = "singularity"
    else: server = "tranquility"

    pathToEve = os.path.expanduser(options.eve)
    pathToCache = os.path.expanduser(options.cache)
    pathToDump = os.path.expanduser(options.dump)
    metadata = {}

    config = ConfigParser()
    config.read(os.path.join(pathToEve, "common.ini"))
    metadata["version"] = config.getint("main", "build")
    metadata["release"] = options.release

    #paths are taken from cmdline arguments
    eve = blue.EVE(pathToEve, cachepath = pathToCache, server = server)
    cfg = eve.getconfigmgr()

    if os.path.exists(pathToDump):
        os.remove(pathToDump)

    conn = sqlite3.connect(pathToDump)
    c = conn.cursor()
    #create structure
    for statement in schema.split(";\n"):
        c.execute(statement)
    #fill with some static data (can't find where we can get it from reverence)
    for statement in staticData.split(";\n"):
        c.execute(statement)
    #create table for version and put some  data into it
    c.execute(metadataTable)
    query = "INSERT INTO dumpmetadata (fieldName, fieldValue) VALUES(?,?)"
    for fieldName in metadata.iterkeys():
        c.execute(query, (fieldName, metadata[fieldName]))

    #Warn about new tables in cache
    for table in cfg.tables:
        if not table in tableMap.iterkeys():
            print "Warning: unmapped table", table

    #compose list of tables from table map, filter those which have None interest for us
    tableNameList = []
    for table in tableMap.iterkeys():
        if tableMap[table] != None: tableNameList.append(table)

    #get data from cache (needs just login) and write it
    for tableName in tableNameList:
        sourceTable = getattr(cfg, tableName)
        processTable(sourceTable, tableName)

    #market needs to be invited separately (do not forget to open it ingame to cache it)
    marketTable = eve.RemoteSvc("marketProxy").GetMarketGroups()
    processTable(marketTable, "invmarketgroups")

    conn.commit()
    conn.close()
