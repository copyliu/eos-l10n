from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table
from sqlalchemy.orm import relation, mapper, synonym

import __init__ as db
from ..types import Category, Group, Icon

categories_table = Table("invcategories", db.meta,
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
