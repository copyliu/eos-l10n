import sqlite3
import os.path
import copy
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--database", help="path to eve cache data dump in \
sqlite format, default eos database path is used if none specified",
type="string", default=os.path.join("~", ".pyfa","eve.db"))
parser.add_option("-a", "--attr", help="find items with this attribute",
type="string", default="")
parser.add_option("-s", "--srq", help="find items with this skill requirement",
type="string", default="")
parser.add_option("-g", "--grp", help="find items from this group",
type="string", default="")
(options, args) = parser.parse_args()

if not options.attr:
    import sys

    sys.stderr.write("You need to specify at attribute name.\n")
    sys.exit()

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
# Limit categories to Celestials (2, only for wormhole effects),
# Ships (6), Modules (7), Charges (8), Skills (16), Drones (18),
# Implants (20), Subsystems (32)
QUERY_PUBLISHEDTYPEIDS = 'SELECT it.typeID FROM invtypes AS it INNER JOIN \
invgroups AS ig ON it.groupID = ig.groupID INNER JOIN invcategories AS ic ON \
ig.categoryID = ic.categoryID WHERE it.published = 1 AND ic.categoryID IN \
(2, 6, 7, 8, 16, 18, 20, 32)'
QUERY_ATTRIBUTEID_TYPEID = "SELECT it.typeID FROM invtypes AS it INNER JOIN \
dgmtypeattribs AS dta ON it.typeID = dta.typeID INNER JOIN dgmattribs AS da \
ON dta.attributeID = da.attributeID WHERE da.attributeName = ?"
QUERY_TYPEID_GROUPID = 'SELECT groupID FROM invtypes WHERE typeID = ? LIMIT 1'
QUERY_GROUPID_CATEGORYID = 'SELECT categoryID FROM invgroups WHERE \
groupID = ? LIMIT 1'
QUERY_TYPEID_PARENTTYPEID = 'SELECT parentTypeID FROM invmetatypes WHERE \
typeID = ? LIMIT 1'
QUERY_TYPEID_SKILLRQ = 'SELECT dta.value FROM dgmtypeattribs AS dta INNER JOIN \
dgmattribs AS da ON da.attributeID = dta.attributeID WHERE (da.attributeName = \
"requiredSkill1" OR da.attributeName = "requiredSkill2" OR da.attributeName = \
"requiredSkill3") AND dta.typeID = ?'
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

QUERY_TYPENAME_TYPEID = 'SELECT typeID FROM invtypes WHERE typeName = ?'
QUERY_GROUPNAME_GROUPID = 'SELECT groupID FROM invgroups WHERE groupName = ?'

if options.srq:
    global_skillrqid = 0
    cursor.execute(QUERY_TYPENAME_TYPEID, (options.srq,))
    for row in cursor:
        global_skillrqid = row[0]
    if not global_skillrqid:
        import sys
        sys.stderr.write("You need to specify proper skill requirement name.\n")
        sys.exit()

if options.grp:
    grouplist = []
    cursor.execute(QUERY_GROUPNAME_GROUPID, (options.grp,))
    for row in cursor:
        grouplist.append(row[0])
    if len(grouplist) > 1:
        print("Warning: multiple groups found, using ID", grouplist[0])
    elif len(grouplist) == 0:
        import sys
        sys.stderr.write("You need to specify proper group name.\n")
        sys.exit()
    global_groupid = grouplist[0]

# Published types set
publishedtypes = set()
cursor.execute(QUERY_PUBLISHEDTYPEIDS)
for row in cursor:
    publishedtypes.add(row[0])

typeswithattr = set()
cursor.execute(QUERY_ATTRIBUTEID_TYPEID, (options.attr,))
for row in cursor:
    if row[0] in publishedtypes:
        typeswithattr.add(row[0])
if len(typeswithattr) == 0:
    import sys
    sys.stderr.write("No items found with this attribute.\n")
    sys.exit()

# Compose group maps
# { groupid : set(typeid) }
map_groupid_typeid = {}
# { typeid : groupid }
map_typeid_groupid = {}
for typeid in typeswithattr:
    groupid = 0
    cursor.execute(QUERY_TYPEID_GROUPID, (typeid,))
    for row in cursor:
        groupid = row[0]
    if not groupid in map_groupid_typeid:
        map_groupid_typeid[groupid] = set()
    map_groupid_typeid[groupid].add(typeid)
    map_typeid_groupid[typeid] = groupid

# Category maps
# { categoryid : set(typeid) }
map_categoryid_typeid =  {}
# { typeid : categoryid }
map_typeid_categoryid =  {}
for typeid in typeswithattr:
    categoryid = 0
    cursor.execute(QUERY_GROUPID_CATEGORYID,
                   (map_typeid_groupid[typeid],))
    for row in cursor:
        categoryid = row[0]
    if not categoryid in map_categoryid_typeid:
        map_categoryid_typeid[categoryid] = set()
    map_categoryid_typeid[categoryid].add(typeid)
    map_typeid_categoryid[typeid] = categoryid

# Skill required maps
# { skillid : set(typeid) }
map_skillrq_typeid =  {}
# { typeid : set(skillid) }
map_typeid_skillrq =  {}
for typeid in typeswithattr:
    cursor.execute(QUERY_TYPEID_SKILLRQ, (typeid,))
    for row in cursor:
        skillid = row[0]
        if not skillid in map_skillrq_typeid:
            map_skillrq_typeid[skillid] = set()
        map_skillrq_typeid[skillid].add(typeid)
        if not typeid in map_typeid_skillrq:
            map_typeid_skillrq[typeid] = set()
        map_typeid_skillrq[typeid].add(skillid)

def gettypename(typeid):
    typename = ""
    cursor.execute(QUERY_TYPEID_TYPENAME, (typeid,))
    for row in cursor:
        typename = row[0]
    return typename

def getgroupname(typeid):
    typename = ""
    cursor.execute(QUERY_GROUPID_GROUPNAME, (typeid,))
    for row in cursor:
        typename = row[0]
    return typename

if options.grp and options.srq:
    # Set of items which are supposed to be affected
    targetitems = map_groupid_typeid[global_groupid].intersection(map_skillrq_typeid[global_skillrqid])
    # All skill requirements of items which are supposed to be affected
    targetitems_skillrqs = set()
    for itemid in targetitems:
        targetitems_skillrqs.update(map_typeid_skillrq[itemid])
    # Remove skill requirement supplied as argument to script
    # we can use that argument when needed manually, and it
    # covers all targetitems which we don't want to do with single skill
    targetitems_skillrqs.remove(global_skillrqid)
    # Print items which are supposed to be affected
    print("Affected items, supposed set ({0} group, {1} skill requirements):".format(getgroupname(global_groupid), gettypename(global_skillrqid)))
    for item in sorted(targetitems, key=lambda item: gettypename(item)):
        print("  {0}".format(gettypename(item)))
    # Cycle through all required skills
    for skillrq in sorted(targetitems_skillrqs, key=lambda sk: gettypename(sk)):
        print("Test any item requiring {0} skill:".format(gettypename(skillrq)))
        for item in sorted(targetitems.intersection(map_skillrq_typeid[skillrq]), key=lambda item: gettypename(item)):
            # If item has 3rd skill requirement (besides supplied as argument and
            # included into header of current section), mention it
            if len(map_typeid_skillrq[item]) == 3:
                otherskillrq = copy.deepcopy(map_typeid_skillrq[item])
                otherskillrq.discard(skillrq)
                otherskillrq.discard(global_skillrqid)
                print("  {0} ({1})".format(gettypename(item), ", ".join(sorted(gettypename(id) for id in otherskillrq))))
            # Just print item names if there're only 2 skill requirements
            elif len(map_typeid_skillrq[item]) == 2:
                print("  {0}".format(gettypename(item)))
            else:
                print("Bad things happened, we never should get here")

    nonaffected = None

elif options.grp:
    # Set of items which are supposed to be affected
    targetitems = copy.deepcopy(map_groupid_typeid[global_groupid])
    # All skill requirements of items which are supposed to be affected
    targetitems_skillrqs = set()
    for itemid in targetitems:
        targetitems_skillrqs.update(map_typeid_skillrq[itemid])
    # Print items which are supposed to be affected
    print("Affected items, supposed set ({0} group):".format(getgroupname(global_groupid)))
    for item in sorted(targetitems, key=lambda item: gettypename(item)):
        print("  {0}".format(gettypename(item)))
    # Cycle through all required skills
    for skillrq in sorted(targetitems_skillrqs, key=lambda sk: gettypename(sk)):
        print("Test any item requiring {0} skill:".format(gettypename(skillrq)))
        for item in sorted(targetitems.intersection(map_skillrq_typeid[skillrq]), key=lambda item: gettypename(item)):
            # If item has other skill requirements, print them
            if len(map_typeid_skillrq[item]) == 3 or len(map_typeid_skillrq[item]) == 2:
                otherskillrq = copy.deepcopy(map_typeid_skillrq[item])
                otherskillrq.discard(skillrq)
                print("  {0} ({1})".format(gettypename(item), ", ".join(sorted(gettypename(id) for id in otherskillrq))))
            # Just print item names if there're only 2 skill requirements
            elif len(map_typeid_skillrq[item]) == 1:
                print("  {0}".format(gettypename(item)))
            else:
                print("Bad things happened, we never should get here")


    nonaffected = None

elif options.srq:
    # Set of items which are supposed to be affected
    targetitems = copy.deepcopy(map_skillrq_typeid[global_skillrqid])
    # All groups of items which are supposed to be affected
    targetitems_groups = set()
    for itemid in targetitems:
        targetitems_groups.add(map_typeid_groupid[itemid])
    # Print items which are supposed to be affected
    print("Affected items, supposed set (with {0} skill requirement):".format(gettypename(global_skillrqid)))
    for item in sorted(targetitems, key=lambda item: gettypename(item)):
        print("  {0}".format(gettypename(item)))
    # Cycle through groups
    for groupid in sorted(targetitems_groups, key=lambda grp: getgroupname(grp)):
        print("Test any item from {0} group:".format(getgroupname(groupid)))
        for item in sorted(targetitems.intersection(map_groupid_typeid[groupid]), key=lambda item: gettypename(item)):
            print("  {0}".format(gettypename(item)))

    nonaffected = None

else:
    affected = typeswithattr
    nonaffected = set()



## Base type maps
## { basetypeid : set(typeid) }
#map_basetypeid_typeid =  {}
## { typeid : basetypeid }
#map_typeid_basetypeid =  {}
#for typeid in typeswithattr:
#    # Not all typeIDs in the database have baseTypeID, so assign some
#    # default value to it
#    basetypeid = 0
#    cursor.execute(QUERY_TYPEID_PARENTTYPEID, (typeid,))
#    for row in cursor:
#        basetypeid = row[0]
#    # If base type is not published or is not set in database, consider
#    # item as variation of self
#    if basetypeid not in typeswithattr:
#        basetypeid = typeid
#    if not basetypeid in map_basetypeid_typeid:
#        map_basetypeid_typeid[basetypeid] = set()
#    map_basetypeid_typeid[basetypeid].add(typeid)
#    map_typeid_basetypeid[typeid] = basetypeid
## Market group maps - we won't use these for further processing, but
## just as helper for composing other maps
## { marketgroupid : set(typeid) }
#map_marketgroupid_typeid =  {}
## { typeid : set(marketgroupid) }
#map_typeid_marketgroupid =  {}
#for typeid in typeswithattr:
#    marketgroupid = 0
#    cursor.execute(QUERY_TYPEID_MARKETGROUPID, (typeid,))
#    for row in cursor:
#        marketgroupid = row[0]
#    if not marketgroupid:
#        continue
#    if not marketgroupid in map_marketgroupid_typeid:
#        map_marketgroupid_typeid[marketgroupid] = set()
#    map_marketgroupid_typeid[marketgroupid].add(typeid)
## Copy items to all parent market groups
#INITIALMARKETGROUPIDS = tuple(map_marketgroupid_typeid)
#for marketgroupid in INITIALMARKETGROUPIDS:
#    # Limit depths for case if database will refer to groups making
#    # the loop
#    cyclingmarketgroupid = marketgroupid
#    for depth in range(20):
#        cursor_parentmarket = db.cursor()
#        cursor_parentmarket.execute(QUERY_MARKETGROUPID_PARENTGROUPID,
#                                    (cyclingmarketgroupid,))
#        for row in cursor_parentmarket:
#            cyclingmarketgroupid = row[0]
#        if cyclingmarketgroupid:
#            if not cyclingmarketgroupid in map_marketgroupid_typeid:
#                map_marketgroupid_typeid[cyclingmarketgroupid] = set()
#            map_marketgroupid_typeid[cyclingmarketgroupid].update\
#            (map_marketgroupid_typeid[marketgroupid])
#        else: break
## Now, make a reverse map
#for marketgroupid, typeidset in map_marketgroupid_typeid.items():
#    for typeid in typeidset:
#        if not typeid in map_typeid_marketgroupid:
#            map_typeid_marketgroupid[typeid] = set()
#        map_typeid_marketgroupid[typeid].add(marketgroupid)
#
## Combine market groups and variations
## { marketgroupid : set(typeidwithvariations) }
#map_marketgroupid_typeidwithvariations = \
#copy.deepcopy(map_marketgroupid_typeid)
## { typeidwithvariations : set(marketgroupid) }
#map_typeidwithvariations_marketgroupid = {}
#for marketgroupid in map_marketgroupid_typeidwithvariations:
#    typestoadd = set()
#    for typeid in map_marketgroupid_typeidwithvariations[marketgroupid]:
#        if typeid in map_basetypeid_typeid:
#            for variationid in map_basetypeid_typeid[typeid]:
#                # Do not include items which have market group, even if
#                # they're variation
#                if variationid in map_typeid_marketgroupid:
#                    typestoadd.add(variationid)
#    map_marketgroupid_typeidwithvariations[marketgroupid].update\
#    (typestoadd)
## Make reverse map using simple way too
#for marketgroupid, typeidwithvariationsset in \
#map_marketgroupid_typeidwithvariations.items():
#    for typeid in typeidwithvariationsset:
#        if not typeid in map_typeidwithvariations_marketgroupid:
#            map_typeidwithvariations_marketgroupid[typeid] = set()
#        map_typeidwithvariations_marketgroupid[typeid].add(marketgroupid)
