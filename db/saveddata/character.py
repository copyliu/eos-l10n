from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import Character

characters_table = Table("characters", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("name", String),
                         Column("apiKey", String),
                         Column("owner", ForeignKey("users.ID")))

skills_table = Table("characterSkills", saveddata_meta,
                     Column("characterID", ForeignKey("characters.ID"), primary_key = True),
                     Column("skillID", Integer, primary_key = True),
                     Column("level"), Integer)

#mapper(Character, characters_table, properties =
#       {"skills" : relation(Integer, primaryjoin = characters_table.c.ID == skills_table.c.characterID, primary = skills_table, foreign_keys = (skills_table.c.skillID,))})