from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection

from model.db import gamedata_meta
from model.types import Icon, Attribute, Item, Effect, MetaGroup

items_table = Table("invtypes", gamedata_meta,
                    Column("typeID", Integer, primary_key = True),
                    Column("typeName", String),
                    Column("description", String),
                    Column("raceID", Integer),
                    Column("published", Boolean),
                    Column("marketGroupID", Integer, ForeignKey("invmarketgroups.marketGroupID")),
                    Column("iconID", Integer, ForeignKey("icons.iconID")),
                    Column("groupID", Integer, ForeignKey("invgroups.groupID")))

from .metagroup import metatypes_table
from .effect import typeeffects_table, effects_table
mapper(Item, items_table, 
       properties = {"icon" : relation(Icon),
                     "attributes" : relation(Attribute, collection_class = attribute_mapped_collection('name')),
                     "effects" : relation(Effect, collection_class = attribute_mapped_collection('name'),
                                          primaryjoin = typeeffects_table.c.typeID == items_table.c.typeID,
                                          secondaryjoin = effects_table.c.effectID == typeeffects_table.c.effectID,
                                          secondary = typeeffects_table),
                     "metaGroup" : relation(MetaGroup,
                                            primaryjoin = metatypes_table.c.typeID == items_table.c.typeID,
                                            uselist = False),
                     "ID" : synonym("typeID"),
                     "name" : synonym("typeName")})

Item.category = association_proxy("group", "category")