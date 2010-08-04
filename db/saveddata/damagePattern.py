#===============================================================================
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
from model.types import DamagePattern

damagePatterns_table = Table("damagePatterns", saveddata_meta,
                             Column("ID", Integer, primary_key = True),
                             Column("emAmount", Integer),
                             Column("thermalAmount", Integer),
                             Column("kineticAmount", Integer),
                             Column("explosiveAmount", Integer),
                             Column("ownerID", ForeignKey("users.ID"), nullable=True))

mapper(DamagePattern, damagePatterns_table)