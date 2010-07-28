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
       properties = {"_Fit__modules" : relation(Module, backref = "fit", collection_class = HandledList,
                                                primaryjoin = and_(modules_table.c.fitID == fits_table.c.ID, modules_table.c.projected == False)),
                     "_Fit__projectedModules" : relation(Module, backref = "target", collection_class = HandledProjectedModList,
                                                primaryjoin = and_(modules_table.c.fitID == fits_table.c.ID, modules_table.c.projected == True)),
                     "_Fit__owner" : relation(User, backref = "fits"),
                     "_Fit__boosters" : relation(Booster, backref = "fit", collection_class = HandledImplantBoosterList),
                     "_Fit__drones" : relation(Drone, backref = "fit", collection_class = HandledDroneList,
                                               primaryjoin = and_(drones_table.c.fitID == fits_table.c.ID, drones_table.c.projected == False)),
                     "_Fit__projectedDrones" : relation(Drone, backref = "target", collection_class = HandledProjectedDroneList,
                                               primaryjoin = and_(drones_table.c.fitID == fits_table.c.ID, drones_table.c.projected == True)),
                     "_Fit__implants" : relation(Implant, backref = "fit", collection_class = HandledImplantBoosterList),
                     "_Fit__character" : relation(Character),
                     "_Fit__projectedFits" : relation(Fit,
                                                      primaryjoin = projectedFits_table.c.victimID == fits_table.c.ID,
                                                      secondaryjoin = fits_table.c.ID == projectedFits_table.c.sourceID,
                                                      secondary = projectedFits_table,
                                                      collection_class = HandledProjectedFitList)
                     })