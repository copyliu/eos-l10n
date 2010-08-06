#===============================================================================
# Copyright (C) 2010  Duclos Diego
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

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym

from model.db import gamedata_meta
from model.types import Item, MarketGroup, Icon

marketgroups_table = Table("invmarketgroups", gamedata_meta,
                           Column("marketGroupID", Integer, primary_key = True),
                           Column("marketGroupName", String),
                           Column("description", String),
                           Column("hasTypes", Boolean),
                           Column("parentGroupID", Integer, ForeignKey("invmarketgroups.marketGroupID")),
                           Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(MarketGroup, marketgroups_table,
       properties = {"items" : relation(Item, backref = "marketGroup"),
                     "parent" : relation(MarketGroup, backref = "children", remote_side = [marketgroups_table.c.marketGroupID]),
                     "icon" : relation(Icon),
                     "ID" : synonym("marketGroupID"),
                     "name" : synonym("marketGroupName")})
