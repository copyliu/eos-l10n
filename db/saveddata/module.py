from sqlalchemy import Table, Column, Integer, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import mapper

from model.db import saveddata_meta
from model.types import Module

modules_table = Table("modules", saveddata_meta,
                      Column("ID", Integer, primary_key = True),
                      Column("fitID", Integer, ForeignKey("fits.ID"), nullable = False),
                      Column("itemID", Integer, nullable = False),
                      Column("chargeID", Integer),
                      Column("state", Integer, CheckConstraint("state >= -1"), CheckConstraint("state <= 2")),
                      Column("projected", Boolean, default = False, nullable = False))

mapper(Module, modules_table)
