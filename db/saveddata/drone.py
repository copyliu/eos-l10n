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

from sqlalchemy import Table, Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import mapper
from model.db import saveddata_meta
from model.types import Drone

drones_table = Table("drones", saveddata_meta,
                     Column("fitID", Integer, ForeignKey("fits.ID"), primary_key = True),
                     Column("itemID", Integer, primary_key = True),
                     Column("amount", Integer, nullable = False),
                     Column("amountActive", Integer, nullable = False),
                     Column("projected", Boolean, default = False, primary_key = True))

mapper(Drone, drones_table)
