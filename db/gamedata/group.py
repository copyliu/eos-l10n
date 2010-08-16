#===============================================================================
# Copyright (C) 2010 Diego Duclos
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

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym

from eos.db import gamedata_meta
from eos.types import Item, Group, Icon

groups_table = Table("invgroups", gamedata_meta,
                     Column("groupID", Integer, primary_key = True),
                     Column("groupName", String),
                     Column("description", String),
                     Column("published", Boolean),
                     Column("categoryID", Integer, ForeignKey("invcategories.categoryID")),
                     Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(Group, groups_table,
       properties = {"items" : relation(Item, backref = "group"),
                     "icon" : relation(Icon, lazy=False),
                     "ID" : synonym("groupID"),
                     "name" : synonym("groupName")})
