from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey
from sqlalchemy.orm import mapper, join, synonym
from ..types import Effect
import __init__ as db

typeeffects_table = Table("dgmtypeeffects", db.meta,
                          Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                          Column("effectID", Integer))

effects_table = Table("dgmeffects", db.meta,
                      Column("effectID", Integer, primary_key = True),
                      Column("effectName", String),
                      Column("description", String),
                      Column("published", Boolean))


j = join(typeeffects_table, effects_table, typeeffects_table.c.effectID == effects_table.c.effectID)
mapper(Effect, j,
       properties = {"ID" : synonym("effectID"),
                     "name" : synonym("effectName")})