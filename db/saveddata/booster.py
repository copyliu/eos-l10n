from sqlalchemy import Table, Column, Integer, ForeignKeyConstraint
from sqlalchemy.orm import mapper

from model.db import saveddata_meta
from model.types import Booster

boosters_table = Table("boosters", saveddata_meta,
                       Column("fitID", Integer, primary_key = True),
                       Column("boosterID", Integer, primary_key = True))

boosters_activesideeffects_table = Table("boosterActiveSideEffects", saveddata_meta,
                                         Column("fitID", Integer),
                                         Column("boosterID", Integer),
                                         Column("activeSideEffect", String),
                                         ForeignKeyConstraint(["fitID", "boosterID"], ["boosters.fitID", "boosters.boosterID"]))

mapper(Booster, boosters_table)