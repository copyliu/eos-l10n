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

from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey
from sqlalchemy.orm import mapper, join, synonym
from model.types import Effect
from model.db import gamedata_meta

typeeffects_table = Table("dgmtypeeffects", gamedata_meta,
                          Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                          Column("effectID", Integer, ForeignKey("dgmeffects.effectID")))

effects_table = Table("dgmeffects", gamedata_meta,
                      Column("effectID", Integer, primary_key = True),
                      Column("effectName", String),
                      Column("description", String),
                      Column("published", Boolean))


mapper(Effect, effects_table,
       properties = {"ID" : synonym("effectID"),
                     "name" : synonym("effectName")})
