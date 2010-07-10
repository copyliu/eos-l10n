from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapper

from model.db import saveddata_meta
from model.types import Skill

skills_table = Table("characterSkills", saveddata_meta,
                     Column("characterID", ForeignKey("characters.ID"), primary_key = True),
                     Column("itemID", Integer, primary_key = True),
                     Column("level", Integer, nullable = False))

mapper(Skill, skills_table)