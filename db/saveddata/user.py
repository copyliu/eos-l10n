from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym

from model.db import saveddata_meta
from model.types import User

users_table = Table("users", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("username", String, nullable = False, unique = True),
                         Column("password", String, nullable = False),
                         Column("admin", Boolean, nullable = False))

mapper(User, users_table)