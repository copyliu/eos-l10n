from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table
from sqlalchemy.orm import relation, mapper, synonym

from model.db import gamedata_meta
from model.types import Category, Group, Icon

categories_table = Table("invcategories", gamedata_meta,
                         Column("categoryID", Integer, primary_key = True),
                         Column("categoryName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(Category, categories_table,
       properties = {"groups" : relation(Group, backref = "category"),
                     "icon" : relation(Icon),
                     "ID" : synonym("categoryID"),
                     "name" : synonym("categoryName")})
