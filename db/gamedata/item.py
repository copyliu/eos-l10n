#===============================================================================
# Copyright (C) 2010 Diego Duclos
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

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection

from eos.db import gamedata_meta
from eos.types import Icon, Attribute, Item, Effect, MetaGroup, Group

items_table = Table("invtypes", gamedata_meta,
                    Column("typeID", Integer, primary_key = True),
                    Column("typeName", String),
                    Column("description", String),
                    Column("raceID", Integer),
                    Column("volume", Integer),
                    Column("capacity", Integer),
                    Column("published", Boolean),
                    Column("marketGroupID", Integer, ForeignKey("invmarketgroups.marketGroupID")),
                    Column("iconID", Integer, ForeignKey("icons.iconID")),
                    Column("groupID", Integer, ForeignKey("invgroups.groupID")))

from .metagroup import metatypes_table
from .effect import typeeffects_table, effects_table
mapper(Item, items_table,
       properties = {"group" : relation(Group, backref = "items", lazy=False),
                     "icon" : relation(Icon, lazy=False),
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
