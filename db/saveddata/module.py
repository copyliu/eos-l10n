from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import Module

modules_table = Table("modules", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("itemID", Integer, nullable = False),
                         Column("ammoID", Integer, nullable = False))

mapper(Module, modules_table)