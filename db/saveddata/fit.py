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
from sqlalchemy.sql import and_

from model.db import saveddata_meta
from model.db.saveddata.module import modules_table
from model.db.saveddata.drone import drones_table
from model.types import Fit, Module, User, Booster, Drone, Implant, Character
from model.effectHandlerHelpers import HandledList
from model.saveddata.fit import HandledDroneList, HandledImplantBoosterList, HandledProjectedModList, HandledProjectedDroneList, HandledProjectedFitList

fits_table = Table("fits", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False),
                         Column("shipID", Integer, nullable = False),
                         Column("name", String, nullable = False),
                         Column("characterID", ForeignKey("characters.ID"), nullable = True))

projectedFits_table = Table("projectedFits", saveddata_meta,
                            Column("sourceID", ForeignKey("fits.ID"), primary_key = True),
                            Column("victimID", ForeignKey("fits.ID"), primary_key = True),
                            Column("amount", Integer))
mapper(Fit, fits_table,
       properties = {"_Fit__modules" : relation(Module, collection_class = HandledList,
                                                primaryjoin = and_(modules_table.c.fitID == fits_table.c.ID, modules_table.c.projected == False)),
                     "_Fit__projectedModules" : relation(Module, collection_class = HandledProjectedModList,
                                                primaryjoin = and_(modules_table.c.fitID == fits_table.c.ID, modules_table.c.projected == True)),
                     "_Fit__owner" : relation(User, backref = "fits"),
                     "_Fit__boosters" : relation(Booster, collection_class = HandledImplantBoosterList),
                     "_Fit__drones" : relation(Drone, collection_class = HandledDroneList,
                                               primaryjoin = and_(drones_table.c.fitID == fits_table.c.ID, drones_table.c.projected == False)),
                     "_Fit__projectedDrones" : relation(Drone, collection_class = HandledProjectedDroneList,
                                               primaryjoin = and_(drones_table.c.fitID == fits_table.c.ID, drones_table.c.projected == True)),
                     "_Fit__implants" : relation(Implant, collection_class = HandledImplantBoosterList),
                     "_Fit__character" : relation(Character),
                     "_Fit__projectedFits" : relation(Fit,
                                                      primaryjoin = projectedFits_table.c.victimID == fits_table.c.ID,
                                                      secondaryjoin = fits_table.c.ID == projectedFits_table.c.sourceID,
                                                      secondary = projectedFits_table,
                                                      collection_class = HandledProjectedFitList)
                     })