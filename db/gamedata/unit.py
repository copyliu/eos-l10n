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

from sqlalchemy import Column, Table, Integer, String
from sqlalchemy.orm import synonym

from eos.db import gamedata_meta, gamedata_session
from eos.types import Unit

groups_table = Table("eveunits", gamedata_meta,
                     Column("unitID", Integer, primary_key = True),
                     Column("unitName", String),
                     Column("displayName", String))

gamedata_session.mapper(Unit, groups_table,
       properties = {"ID" : synonym("unitID"),
                     "name" : synonym("unitName")})
