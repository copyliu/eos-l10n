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

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relation, mapper

from model.db import saveddata_meta
from model.types import Character, User, Skill

characters_table = Table("characters", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("name", String, nullable = False),
                         Column("apiID", Integer),
                         Column("apiKey", String),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False))

mapper(Character, characters_table,
       properties = {"_Character__owner" : relation(User, backref = "characters"),
                     "_Character__skills" : relation(Skill, collection_class = set)})
