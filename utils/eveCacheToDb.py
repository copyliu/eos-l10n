#!/usr/bin/env python
#===============================================================================
# Copyright (C) 2010 Anton Vorobyov
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
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
This script pulls data out of EVE cache and makes an SQLite dump
Reverence library by Entity is used, check http://wiki.github.com/ntt/reverence/ for info
As reverence uses the same python version as EVE client (2.x series), script cannot be converted to python3
Example commands to run the script for default paths:
Tranquility: python eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_tranquility/cache" --dump="~/Desktop/eve.db"
Singularity: python eveCacheToSqlite.py --eve="~/.wine/drive_c/Program Files/CCP/EVE (Singularity)" --cache="~/.wine/drive_c/users/"$USER"/Local Settings/Application Data/CCP/EVE/c_program_files_ccp_eve_(singularity)_singularity/cache" --sisi --dump="~/Desktop/evetest.db"
'''

import sys, os
#Add the good path to sys.path
path = os.path.dirname(unicode(__file__, sys.getfilesystemencoding()))
sys.path.append(os.path.realpath(os.path.join(path, "..", "..")))

def get_map():
    return {"allianceshortnames": None,
            "billtypes": None,
            "certificaterelationships": None,
            "certificates": None,
            "corptickernames": None,
            "dgmattribs": AttributeInfo,
            "dgmeffects": EffectInfo,
            "dgmtypeattribs": Attribute,
            "dgmtypeeffects": Effect,
            "evegraphics": None,
            "evelocations": None,
            "eveowners": None,
            "eveunits": Unit,
            "groupsByCategories": None,
            "icons": Icon,
            "invbptypes": None,
            "invcategories": Category,
            "invcontrabandTypesByFaction": None,
            "invcontrabandTypesByType": None,
            "invgroups": Group,
            "invmetagroups": MetaGroup,
            "invmetatypes": MetaType,
            "invmetatypesByTypeID": None,
            "invreactiontypes": None,
            "invtypes": Item,
            "locationscenes": None,
            "locationwormholeclasses": None,
            "mapcelestialdescriptions": None,
            "ownericons": None,
            "ramactivities": None,
            "ramaltypes": None,
            "ramaltypesdetailpercategory": None,
            "ramaltypesdetailpergroup": None,
            "ramcompletedstatuses": None,
            "ramtypematerials": None,
            "ramtyperequirements": None,
            "schematics": None,
            "schematicsByPin": None,
            "schematicsByType": None,
            "schematicspinmap": None,
            "schematicstypemap": None,
            "shiptypes": None,
            "sounds": None,
            "typesByGroups": None,
            "typesByMarketGroups": None}

def get_order():
    return ("icons",
            "eveunits",
            "dgmattribs",
            "dgmeffects",
            "invcategories",
            "invgroups",
            "invmetagroups",
            "invmetatypes",
            "invtypes",
            "dgmtypeattribs",
            "dgmtypeeffects")

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

def process_table(sourcetable, tablename, tableclass):
    """
    Get all data from cache and write it to database
    """
    # Get data from source and process it
    tabledata = get_table_data(sourcetable, tablename, get_source_headers(sourcetable))
    # Insert everything into table
    insert_table_values(tabledata, tableclass)

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
                    datarow[headerlist[i]] = unicode(values[i], 'ISO-8859-1')
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

def insert_table_values(tabledata, tableclass):
    for row in tabledata:
        instance = tableclass()
        for header in row:
            setattr(instance, header, process_value(row[header]))

        eos.db.gamedata_session.add(instance)

    eos.db.gamedata_session.commit()

def process_value(value):
    if value == 0:
        return None
    else:
        return value
if __name__ == "__main__":
    import os
    import re
    import sqlite3
    import sys
    from ConfigParser import ConfigParser
    from optparse import OptionParser
    from reverence import blue
    import sqlalchemy
    import eos.config
    from sqlalchemy import Column, Table, String
    from sqlalchemy.orm import mapper

    # Parse command line options
    usage = "usage: %prog [--old=OLD] --new=NEW [-ear]"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--eve", help="path to eve folder")
    parser.add_option("-c", "--cache", help="path to eve cache folder")
    parser.add_option("-d", "--dump", help="the sqlalchemy connectionstring of where we should place our stuff")
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

    eos.config.gamedata_connectionstring = PATH_DUMP

    from eos.gamedata import *
    import eos.db

    # Get version of EVE client
    config = ConfigParser()
    config.read(os.path.join(PATH_EVE, "common.ini"))

    # Form metadata dictionary for corresponding table
    metadata = {}
    metadata["version"] = config.getint("main", "build")
    metadata["release"] = options.release

    # Initialize Reverence ccache manager
    eve = blue.EVE(PATH_EVE, cachepath=PATH_CACHE, server=server)
    cfg = eve.getconfigmgr()

    #Add a custom metadata table
    class MetaData(object):
        def __init__(self, name, val):
            self.fieldName = name
            self.fieldValue = val

    metadata_table = Table("metadata", eos.db.gamedata_meta,
                           Column("fieldName", String, primary_key=True),
                           Column("fieldValue", String))

    mapper(MetaData, metadata_table)

    #Create all our tables now
    eos.db.gamedata_meta.create_all()

    #Add versioning info to the metadata table
    for fieldname in metadata:
        eos.db.gamedata_session.add(MetaData(fieldname, metadata[fieldname]))

    eos.db.gamedata_session.commit()

    #Grab table map
    TABLE_MAP = get_map()
    # Warn about new tables in cache
    for table in cfg.tables:
        if not table in TABLE_MAP:
            print "Warning: unmapped table", table, "found in cache"

    # Warn about missing tables
    for table in TABLE_MAP:
        if not table in cfg.tables:
            print "Warning: mapped table", table, "cannot be found in cache"

    # Get data from cache (you need to just login to eve for cache files to be written) and write it
    for tablename in get_order():
        tableclass = TABLE_MAP[tablename]
        if tableclass is not None:
            print "processing: %s" % (tablename)
            sourceTable = getattr(cfg, tablename)
            process_table(sourceTable, tablename, tableclass)

    # Market needs to be invited separately (do not forget to open it ingame to cache it)
    markettable = eve.RemoteSvc("marketProxy").GetMarketGroups()
    process_table(markettable, "invmarketgroups", MarketGroup)
