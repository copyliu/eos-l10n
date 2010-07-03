from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import Character, User

characters_table = Table("characters", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("name", String, nullable = False),
                         Column("apiKey", String),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False))

mapper(Character, characters_table,
       properties = {"owner" : relation(User, backref = "characters")})