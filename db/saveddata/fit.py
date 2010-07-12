from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relation, mapper

from model.db import saveddata_meta
from model.types import Fit, Module, User, Booster, Drone, Implant
from model.effectHandlerHelpers import HandledList

fits_table = Table("fits", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False),
                         Column("shipID", Integer, nullable = False),
                         Column("name", String, nullable = False))

mapper(Fit, fits_table,
       properties = {"_Fit__modules" : relation(Module, backref = "fit", collection_class = HandledList),
                     "_Fit__owner" : relation(User, backref = "fits", collection_class = HandledList),
                     "_Fit__boosters" : relation(Booster, backref = "fit", collection_class = HandledList),
                     "_Fit__drones" : relation(Drone, backref = "fit", collection_class = HandledList),
                     "_Fit__implants" : relation(Implant, backref = "fit", collection_class = HandledList)})