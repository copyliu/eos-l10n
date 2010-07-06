from sqlalchemy import Table, Column, Integer
from sqlalchemy.orm import mapper

from model.db import saveddata_meta
from model.types import Module

modules_table = Table("modules", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("itemID", Integer, nullable = False),
                         Column("chargeID", Integer, nullable = False))

mapper(Module, modules_table)