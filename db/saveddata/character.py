from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relation, mapper

from model.db import saveddata_meta
from model.types import Character, User, Skill

characters_table = Table("characters", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("name", String, nullable = False),
                         Column("apiKey", String),
                         Column("ownerID", ForeignKey("users.ID"), nullable = False))

mapper(Character, characters_table,
       properties = {"_Character__owner" : relation(User, backref = "characters"),
                     "_Character__skills" : relation(Skill, collection_class = set)})