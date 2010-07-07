from sqlalchemy import Table, Column, ForeignKey, Integer, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import mapper, relation
from sqlalchemy.ext.associationproxy import association_proxy

from model.db import saveddata_meta
from model.types import Booster, Fit

boosters_table = Table("boosters", saveddata_meta,
                       Column("ID", Integer, primary_key = True),
                       Column("itemID", Integer),
                       Column("fitID", Integer, ForeignKey("fits.ID")),
                       UniqueConstraint("itemID", "fitID"))

activeSideEffects_table = Table("boostersActiveSideEffects", saveddata_meta,
                                Column("boosterID", ForeignKey("boosters.ID"), primary_key = True),
                                Column("effectID", Integer, primary_key = True))

class ActiveSideEffectsDummy(object):
    def __init__(self, effectID):
        self.effectID = effectID
        

mapper(ActiveSideEffectsDummy, activeSideEffects_table)
mapper(Booster, boosters_table,
       properties = {"_Booster__activeSideEffectDummies" : relation(ActiveSideEffectsDummy)})

Booster._Booster__activeSideEffectIDs = association_proxy("_Booster__activeSideEffectDummies", "effectID")