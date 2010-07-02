from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import Fit

fits_table = Table("fits", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("character", ForeignKey("users.ID"), nullable = False),
                         Column("shipID", Integer, nullable = False))

fitsmodules_table = Table("fitsModules", saveddata_meta,
                          Column("fitID", ForeignKey("fits.ID"), primary_key = True),
                          Column("moduleID", ForeignKey("modules.ID"), primary_key = True))

mapper(Fit, fits_table)