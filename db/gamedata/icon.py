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

from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import mapper, synonym

from eos.db import gamedata_meta
from eos.types import Icon

icons_table = Table("icons", gamedata_meta,
                    Column("iconID", Integer, primary_key = True),
                    Column("description", String),
                    Column("iconFile", String))

mapper(Icon, icons_table,
       properties = {"ID" : synonym("iconID")})
