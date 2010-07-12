from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapper
from model.db import saveddata_meta
from model.types import Drone

drones_table = Table("drones", saveddata_meta,
                     Column("fitID", Integer, ForeignKey("fits.ID"), primary_key = True),
                     Column("itemID", Integer, primary_key = True),
                     Column("amount", Integer, nullable = False))

mapper(Drone, drones_table)