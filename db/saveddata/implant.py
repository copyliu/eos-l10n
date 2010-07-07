from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapper

from model.db import saveddata_meta
from model.types import Implant

implants_table = Table("implants", saveddata_meta,
                     Column("fitID", Integer, ForeignKey("fits.ID"), primary_key = True),
                     Column("itemID", Integer, primary_key = True))

mapper(Implant, implants_table)