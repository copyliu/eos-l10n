#!/usr/bin/env python2.6
#===============================================================================
# Copyright (C) 2010 Anton Vorobyov
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

'''
This script pulls data out of EVE cache and makes an SQLite dump
Reverence library by Entity is used, check http://wiki.github.com/ntt/reverence/ for info
As reverence uses the same python version as EVE client (2.x series), script cannot be converted to python3
Example commands to run the script for default paths:
Tranquility: python2.6 eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_tranquility/cache" --dump="~/Desktop/eve.db"
Singularity: python2.6 eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE (Singularity)" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_(singularity)_singularity/cache" --sisi --dump="~/Desktop/evetest.db"
'''

SCHEMA = '''
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

CREATE TABLE "eveunits" (
  "unitID" smallint(6) NOT NULL,
  "unitName" varchar(100) default NULL,
  "displayName" varchar(100) default NULL,
  PRIMARY KEY ("unitID")
);

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

STATIC = '''
CREATE TABLE "dgmAttributeCategories" (
  "categoryID" tinyint(3) NOT NULL,
  "categoryName" varchar(50) default NULL,
  "categoryDescription" varchar(200) default NULL,
  PRIMARY KEY ("categoryID")
);
'''

METADATA = '''
CREATE TABLE "metadata" (
  "fieldName" varchar(50) NOT NULL,
  "fieldValue" varchar(100) default NULL,
  PRIMARY KEY ("fieldName")
);
'''

#{ source table name : dest table name }
TABLE_MAP = {
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
"eveunits"                      : "eveunits",
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

def process_table(sourcetable, tablename):
    """
    Get all data from cache and write it to database
    """
    def get_source_headers(sourcetable):
        """
        Pull list of headers from the source table
        """
        sourceheaders = None
        guid = getattr(sourcetable, "__guid__", "None")
        # For IndexRowset and IndexedRowLists Reverence provides list of headers
        if guid in ("util.IndexRowset", "util.FilterRowset"):
            sourceheaders = list(sourcetable.header)
        # For IndexedRowLists, we need to compose list ourselves
        elif guid == "util.IndexedRowLists":
            headerset = set()
            for item in sourcetable:
                for row in sourcetable[item]:
                    for headername in row.__header__.Keys():
                        headerset.add(headername)
            sourceheaders = list(headerset)
        return sourceheaders

    def get_dest_headers(tablename):
        """
        Pull list of headers from database schema
        """
        c.execute("PRAGMA table_info({0})".format(tablename))
        destheaders = [row[1] for row in c]
        return destheaders

    def get_common_headers(sourceheaders, destheaders):
        """
        Compose list of headers common for both source and destination tables
        """
        # Transform lists to sets, find common items and transform back to list
        headerlist = list(frozenset(sourceheaders).intersection(frozenset(destheaders)))
        return headerlist

    def print_noncommon_headers(headerlist, sourceheaders, destheaders, tablename):
        """
        Print list of headers which is ignored for export and import
        """
        ignored_source = frozenset(sourceheaders).difference(frozenset(headerlist))
        ignored_dest = frozenset(destheaders).difference(frozenset(headerlist))
        for sourceheader in sorted(ignored_source):
            print "Warning: data dump schema does not have column for {0}.{1}".format(tablename, sourceheader)
        for destheader in sorted(ignored_dest):
            print "Warning: source does not contain data for {0}.{1}".format(tablename, destheader)
        return

    def get_table_data(sourcetable, tablename, headerlist):
        """
        Pull data out of source table
        """
        # Each row is enclosed into dictionary, full table is list of these dictionaries
        datarows = []
        guid = getattr(sourcetable, "__guid__", "None")
        # We have Select method for IndexRowset tables
        if guid == "util.IndexRowset":
            for values in sourcetable.Select(*headerlist):
                # When Select is asked to find single value, it is returned in its raw
                # form. Convert is to tuple for proper further processing
                if not isinstance(values, (list, tuple, set)):
                    values = (values,)
                headerlistlen = len(headerlist)
                datarow = {}
                # 1 row value should correspond to 1 header, if number or values doesn't
                # correspond to number of headers then something went wrong
                if headerlistlen != len(values):
                    print "Error: malformed data in source table {0}".format(tablename)
                    return None
                # Fill row dictionary with values and append it to list
                for i in xrange(headerlistlen):
                    # If we've got ASCII string, convert it to unicode
                    if isinstance(values[i], str):
                        datarow[headerlist[i]] = values[i].decode('ISO-8859-1')
                    else:
                        datarow[headerlist[i]] = values[i]
                datarows.append(datarow)
        # FilterRowset and IndexedRowLists are accessible almost like dictionaries
        elif guid in ("util.FilterRowset", "util.IndexedRowLists"):
            # Go through all source table elements
            for element in sourcetable.iterkeys():
                # Go through all rows of an element
                for row in sourcetable[element]:
                    datarow = {}
                    # Fill row dictionary with values we need and append it to the list
                    for header in headerlist:
                        value = getattr(row, header, None)
                        # None and zero values are different, and we want to write zero
                        # values to database
                        if value or value in (0, 0.0):
                            datarow[header] = value
                    datarows.append(datarow)
        return datarows

    def process_table_values(tabledata):
        """
        Modify values to satisfy SQL needs
        """
        def convert_list_value(value):
            """
            Convert values for list data type
            """
            if isinstance(value, basestring):
                value = value.replace("'", "''")
            else:
                value = str(value)
            return value

        for row in tabledata:
            for key in row:
                # Text should be in singlequotes with singlequotes escaped by singlequotes
                if isinstance(row[key], basestring):
                    row[key] = u"'{0}'".format(row[key].replace("'", "''"))
                # Bool values are used as tinyint(1) in database; also we
                # convert them to string for proper operation of join in insert function
                elif isinstance(row[key], bool):
                    row[key] = str(int(row[key]))
                # Lists are converted to csv
                elif isinstance(row[key], (list, tuple, set)):
                    row[key] = "'" + u",".join(map(convert_list_value, row[key])) + "'"
                # Pass empty strings to sql in  case of no data
                elif row[key] is None:
                    row[key] = "''"
                # Convert everything else to str for proper operation of join
                else:
                    row[key] = str(row[key])
        return

    def insert_table_values(tabledata, tablename):
        for row in tabledata:
            headers = []
            values = []
            for header in row:
                headers.append(header)
                values.append(row[header])
            query = u"INSERT INTO {0} ({1}) VALUES({2})".format(tablename, u",".join(headers), u",".join(values))
            c.execute(query)
        return

    # Get headers from source table
    sourceheaders = get_source_headers(sourcetable)
    if not sourceheaders:
        print "Error: unknown type for", tablename, "source table"
        return
    # Get column names from database schema
    destheaders = get_dest_headers(tablename)
    # Get map of common headers
    headerlist = get_common_headers(sourceheaders, destheaders)
    # Inform if we have no proper destination for data or source for existing destination
    print_noncommon_headers(headerlist, sourceheaders, destheaders, tablename)
    # Get data from source and process it
    tabledata = get_table_data(sourcetable, tablename, headerlist)
    # Modify data to satisfy SQL query requirements
    process_table_values(tabledata)
    # Insert everything into table
    insert_table_values(tabledata, tablename)
    return

if __name__ == "__main__":
    import os
    import re
    import sqlite3
    import sys
    from ConfigParser import ConfigParser
    from optparse import OptionParser

    from reverence import blue

    # Parse command line options
    usage = "usage: %prog [--old=OLD] --new=NEW [-ear]"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--eve", help="path to eve folder")
    parser.add_option("-c", "--cache", help="path to eve cache folder")
    parser.add_option("-d", "--dump", help="where to data dump file for writing")
    parser.add_option("-r", "--release", help="database release number, defaults to 1", default="1")
    parser.add_option("-s", "--sisi", action="store_true", dest="singularity", help="if you're going to work with singulary test server data, use this option", default=False)
    (options, args) = parser.parse_args()

    # Exit if we do not have any of required options
    if not options.eve or not options.cache or not options.dump:
        sys.stderr.write("You need to specify paths to eve folder, cache folder and dump file. Run script with --help option for further info.\n")
        sys.exit()

    # We can deal either with singularity or tranquility servers
    if options.singularity: server = "singularity"
    else: server = "tranquility"

    # Set static variables for paths
    PATH_EVE = os.path.expanduser(options.eve)
    PATH_CACHE = os.path.expanduser(options.cache)
    PATH_DUMP = os.path.expanduser(options.dump)

    # Get version of EVE client
    config = ConfigParser()
    config.read(os.path.join(PATH_EVE, "common.ini"))

    # Form metadata dictionary for corresponding table
    metadata = {}
    metadata["version"] = config.getint("main", "build")
    metadata["release"] = options.release

    # Initialize Reverence ccache manager
    eve = blue.EVE(PATH_EVE, cachepath = PATH_CACHE, server = server)
    cfg = eve.getconfigmgr()

    # Check if dump file already exists and remove it
    if os.path.exists(PATH_DUMP):
        os.remove(PATH_DUMP)

    # Connect to sqlite dump database
    conn = sqlite3.connect(PATH_DUMP)
    c = conn.cursor()

    # Create structure
    for statement in SCHEMA.split(";\n"):
        c.execute(statement)

    # Fill with some static data (can't find where we can get it from reverence)
    for statement in STATIC.split(";\n"):
        c.execute(statement)

    # Create table for version and put some  data into it
    c.execute(METADATA)
    query = "INSERT INTO metadata (fieldName, fieldValue) VALUES(?,?)"
    for fieldname in metadata:
        c.execute(query, (fieldname, metadata[fieldname]))

    # Warn about new tables in cache
    for table in cfg.tables:
        if not table in TABLE_MAP:
            print "Warning: unmapped table", table, "found in cache"

    # Warn about missing tables
    for table in TABLE_MAP:
        if not table in cfg.tables:
            print "Warning: mapped table", table, "cannot be found in cache"

    # Compose list of tables from table map, filter those which have no interest for us
    tablenames = []
    for table in TABLE_MAP:
        if TABLE_MAP[table] is not None: tablenames.append(table)

    # Get data from cache (you need to just login to eve for cache files to be written) and write it
    for tablename in tablenames:
        sourceTable = getattr(cfg, tablename)
        process_table(sourceTable, tablename)

    # Market needs to be invited separately (do not forget to open it ingame to cache it)
    markettable = eve.RemoteSvc("marketProxy").GetMarketGroups()
    process_table(markettable, "invmarketgroups")

    # Commit results to dump file
    conn.commit()
    conn.close()
