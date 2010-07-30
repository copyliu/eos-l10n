from sqlalchemy import Table, Column, Integer, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import mapper, relation

from model.db import saveddata_meta
from model.types import Gang, Wing, Squad, Fit
from model.db.saveddata.fit import fits_table

gangs_table = Table("gangs", saveddata_meta,
                    Column("ID", Integer, primary_key = True),
                    Column("leaderID", ForeignKey("fits.ID")))

wings_table = Table("wings", saveddata_meta,
                    Column("ID", Integer, primary_key = True),
                    Column("gangID", ForeignKey("gangs.ID")),
                    Column("leaderID", ForeignKey("fits.ID")))

squads_table = Table("squads", saveddata_meta,
                     Column("ID", Integer, primary_key = True),
                     Column("wingID", ForeignKey("wings.ID")),
                     Column("leaderID", ForeignKey("fits.ID")),
                     Column("boosterID", ForeignKey("fits.ID")))

squadmembers_table = Table("squadmembers", saveddata_meta,
                           Column("squadID", ForeignKey("squads.ID"), primary_key = True),
                           Column("memberID", ForeignKey("fits.ID"), primary_key = True))

mapper(Gang, gangs_table,
       properties = {"wings" : relation(Wing, backref="gang"),
                     "leader" : relation(Fit)})

mapper(Wing, wings_table,
       properties = {"squads" : relation(Squad, backref="wing"),
                     "leader" : relation(Fit)})

mapper(Squad, squads_table,
       properties = {"leader" : relation(Fit, primaryjoin = squads_table.c.leaderID == fits_table.c.ID),
                     "booster" : relation(Fit, primaryjoin = squads_table.c.boosterID == fits_table.c.ID),
                     "members" : relation(Fit,
                                          primaryjoin = squads_table.c.ID == squadmembers_table.c.squadID,
                                          secondaryjoin = squadmembers_table.c.memberID == fits_table.c.ID,
                                          secondary = squadmembers_table)})

