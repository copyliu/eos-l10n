from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
from model.types import Attribute, Icon
from model.db import gamedata_meta
typeattributes_table = Table("dgmtypeattribs", gamedata_meta,
                         Column("value", Float),
                         Column("typeID", Integer, ForeignKey("invtypes.typeID")),
                         Column("attributeID", Integer))

attributes_table = Table("dgmattribs", gamedata_meta,
                         Column("attributeID", Integer, primary_key = True),
                         Column("attributeName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("displayName", String),
                         Column("highIsGood", Boolean),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

j = join(typeattributes_table, attributes_table, typeattributes_table.c.attributeID == attributes_table.c.attributeID)
#
mapper(Attribute, j,
       properties = {"icon" : relation(Icon),
                     "ID" : synonym("attributeID"),
                     "name" : synonym("attributeName")})