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

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table
from sqlalchemy.orm import relation, mapper, synonym

from eos.db import gamedata_meta
from eos.types import Category, Group, Icon

categories_table = Table("invcategories", gamedata_meta,
                         Column("categoryID", Integer, primary_key = True),
                         Column("categoryName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(Category, categories_table,
       properties = {"groups" : relation(Group, backref = "category"),
                     "icon" : relation(Icon),
                     "ID" : synonym("categoryID"),
                     "name" : synonym("categoryName")})
