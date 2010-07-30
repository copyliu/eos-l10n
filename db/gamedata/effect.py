from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey
from sqlalchemy.orm import mapper, join, synonym
from model.types import Effect
from model.db import gamedata_meta

typeeffects_table = Table("dgmtypeeffects", gamedata_meta,
                          Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                          Column("effectID", Integer, ForeignKey("dgmeffects.effectID")))

effects_table = Table("dgmeffects", gamedata_meta,
                      Column("effectID", Integer, primary_key = True),
                      Column("effectName", String),
                      Column("description", String),
                      Column("published", Boolean))


mapper(Effect, effects_table,
       properties = {"ID" : synonym("effectID"),
                     "name" : synonym("effectName")})