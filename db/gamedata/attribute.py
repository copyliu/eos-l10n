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

from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
from eos.types import Attribute, Icon
from eos.db import gamedata_meta
typeattributes_table = Table("dgmtypeattribs", gamedata_meta,
                         Column("value", Float),
                         Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                         Column("attributeID", ForeignKey("dgmattribs.attributeID")))

attributes_table = Table("dgmattribs", gamedata_meta,
                         Column("attributeID", Integer, primary_key = True),
                         Column("attributeName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("displayName", String),
                         Column("highIsGood", Boolean),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

j = join(typeattributes_table, attributes_table, typeattributes_table.c.attributeID == attributes_table.c.attributeID)

mapper(Attribute, j,
       primary_key = [typeattributes_table.c.typeID, typeattributes_table.c.attributeID],
       properties = {"icon" : relation(Icon, lazy=False),
                     "name" : synonym("attributeName"),
                     "ID" : synonym("attributeID")})
