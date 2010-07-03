from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import Skill

skills_table = Table("characterSkills", saveddata_meta,
                     Column("characterID", ForeignKey("characters.ID"), primary_key = True),
                     Column("skillID", Integer, primary_key = True),
                     Column("level", Integer, nullable = False))

mapper(Skill, skills_table)