#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relation, mapper, join, synonym
from model.db import gamedata_meta
from model.db.gamedata.item import items_table
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
       primary_key = [metagroups_table.c.metaGroupID, metatypes_table.c.parentTypeID],
       properties = {"ID" : synonym("metaGroupID"),
                     "name" : synonym("metaGroupName"),
                     "parent" : relation(Item, primaryjoin = metatypes_table.c.parentTypeID == items_table.c.typeID),
                     "items" : relation(Item,
                                        primaryjoin = metatypes_table.c.typeID == items_table.c.typeID)})
