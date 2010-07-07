from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relation, mapper

from model.db import saveddata_meta
from model.types import Fit, Module, User, Booster, Drone
from model.db.saveddata.module import modules_table

fits_table = Table("fits", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False),
                         Column("shipID", Integer, nullable = False))

mapper(Fit, fits_table,
       properties = {"_Fit__modules" : relation(Module, backref = "fit"),
                     "_Fit__owner" : relation(User, backref = "fits"),
                     "_Fit__boosters" : relation(Booster, backref = "fit"),
                     "_Fit__drones" : relation(Drone, backref = "fit")})