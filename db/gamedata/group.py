from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym

from model.db import gamedata_meta
from model.types import Item, Group, Icon

groups_table = Table("invgroups", gamedata_meta,
                     Column("groupID", Integer, primary_key = True),
                     Column("groupName", String),
                     Column("description", String),
                     Column("published", Boolean),
                     Column("categoryID", Integer, ForeignKey("invcategories.categoryID")),
                     Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(Group, groups_table, 
       properties = {"items" : relation(Item, backref = "group"),
                     "icon" : relation(Icon),
                     "ID" : synonym("groupID"),
                     "name" : synonym("groupName")})