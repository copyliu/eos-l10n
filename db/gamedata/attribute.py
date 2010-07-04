from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
from sqlalchemy.ext.associationproxy import association_proxy
from model.types import Attribute, Icon
from model.db import gamedata_meta
typeattributes_table = Table("dgmtypeattribs", gamedata_meta,
                         Column("value", Float),
                         Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                         Column("attributeID", ForeignKey("dgmattribs.attributeID")))

attributes_table = Table("dgmattribs", gamedata_meta,
                         Column("attributeID", Integer, primary_key = True),
                         Column("attributeName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("displayName", String),
                         Column("highIsGood", Boolean),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

j = join(typeattributes_table, attributes_table, typeattributes_table.c.attributeID == attributes_table.c.attributeID)

mapper(Attribute, j,
       primary_key = [typeattributes_table.c.typeID, typeattributes_table.c.attributeID],
       properties = {"icon" : relation(Icon),
                     "name" : synonym("attributeName"),
                     "ID" : synonym("attributeID")})