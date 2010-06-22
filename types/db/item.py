from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper
from sqlalchemy.orm.collections import attribute_mapped_collection

import __init__ as db
from ..types import Icon, Attribute, Item, Effect, MetaGroup
from metagroup import metagroups_table, metatypes_table

items_table = Table("invtypes", db.meta,
                    Column("typeID", Integer, primary_key = True),
                    Column("typeName", String),
                    Column("description", String),
                    Column("raceID", Integer),
                    Column("published", Boolean),
                    Column("marketGroupID", Integer, ForeignKey("invmarketgroups.marketGroupID")),
                    Column("iconID", Integer, ForeignKey("icons.iconID")),
                    Column("groupID", Integer, ForeignKey("invgroups.groupID")))

from metagroup import metatypes_table

mapper(Item, items_table, 
       properties = {"icon" : relation(Icon),
                     "attributes" : relation(Attribute, collection_class = attribute_mapped_collection('attributeName')),
                     "effects" : relation(Effect, collection_class = attribute_mapped_collection('effectName')),
                     "metagroup" : relation(MetaGroup,
                                            primaryjoin = items_table.c.typeID == metatypes_table.c.typeID,
                                            secondaryjoin = metatypes_table.c.metaGroupID == metagroups_table.c.metaGroupID,
                                            secondary = metatypes_table,
                                            uselist = False)})