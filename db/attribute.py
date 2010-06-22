from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
from ..types import Attribute, Icon
import __init__ as db

typeattributes_table = Table("dgmtypeattribs", db.meta,
                         Column("value", Float),
                         Column("typeID", Integer, ForeignKey("invtypes.typeID"), primary_key = True),
                         Column("attributeID", Integer, primary_key = True),
                         Column("iconID", Integer, ForeignKey("icons.iconID")))

attributes_table = Table("dgmattribs", db.meta,
                         Column("attributeID", Integer, primary_key = True),
                         Column("attributeName", String),
                         Column("description", String),
                         Column("published", Boolean),
                         Column("displayName", String),
                         Column("highIsGood", Boolean))

j = join(typeattributes_table, attributes_table, typeattributes_table.c.attributeID == attributes_table.c.attributeID)
#
mapper(Attribute, j,
       properties = {"icon" : relation(Icon),
                     "ID" : synonym("attributeID"),
                     "name" : synonym("attributeName")})