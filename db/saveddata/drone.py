from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapper, relation

from model.db import saveddata_meta
from model.types import Drone, Fit

drones_table = Table("drones", saveddata_meta,
                     Column("fitID", Integer, ForeignKey("fits.ID"), primary_key = True),
                     Column("itemID", Integer, primary_key = True),
                     Column("chargeID", Integer),
                     Column("amount", Integer, nullable = False))

mapper(Drone, drones_table)