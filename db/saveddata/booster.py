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

from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint, Boolean
from sqlalchemy.orm import mapper, relation
from sqlalchemy.ext.associationproxy import association_proxy

from model.db import saveddata_meta
from model.types import Booster

boosters_table = Table("boosters", saveddata_meta,
                       Column("ID", Integer, primary_key = True),
                       Column("itemID", Integer),
                       Column("fitID", Integer, ForeignKey("fits.ID"), nullable = False),
                       Column("active", Boolean),
                       UniqueConstraint("itemID", "fitID"))

activeSideEffects_table = Table("boostersActiveSideEffects", saveddata_meta,
                                Column("boosterID", ForeignKey("boosters.ID"), primary_key = True),
                                Column("effectID", Integer, primary_key = True))

class ActiveSideEffectsDummy(object):
    def __init__(self, effectID):
        self.effectID = effectID


mapper(ActiveSideEffectsDummy, activeSideEffects_table)
mapper(Booster, boosters_table,
       properties = {"_Booster__activeSideEffectDummies" : relation(ActiveSideEffectsDummy)})

Booster._Booster__activeSideEffectIDs = association_proxy("_Booster__activeSideEffectDummies", "effectID")
