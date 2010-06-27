from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
from .. import gamedata_meta
from item import items_table
from model.types import MetaGroup, Item

metagroups_table = Table("invmetagroups", gamedata_meta,
                         Column("metaGroupID", Integer, primary_key = True),
                         Column("metaGroupName", String))

metatypes_table = Table("invmetatypes", gamedata_meta,
                        Column("typeID", Integer, ForeignKey("invtypes.typeID"), primary_key = True),
                        Column("parentTypeID", Integer, ForeignKey("invtypes.typeID")),
                        Column("metaGroupID", Integer, ForeignKey("invmetagroups.metaGroupID")))

j = join(metagroups_table, metatypes_table, metatypes_table.c.metaGroupID == metagroups_table.c.metaGroupID)

mapper(MetaGroup, j,
       properties = {"ID" : synonym("metaGroupID"),
                     "name" : synonym("metaGroupName"),
                     "parent" : relation(Item, primaryjoin = metatypes_table.c.parentTypeID == items_table.c.typeID)})