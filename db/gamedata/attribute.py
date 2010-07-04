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

class Association_proxy(object):
    pass

mapper(Association_proxy, attributes_table)

mapper(Attribute, typeattributes_table,
       primary_key=[typeattributes_table.c.typeID, typeattributes_table.c.attributeID],
       properties = {#"icon" : relation(Icon),
                     "attribute_proxy" : relation(Association_proxy)})

Attribute.ID = association_proxy("attribute_proxy", "attributeID")
Attribute.name = association_proxy("attribute_proxy", "attributeName")
Attribute.description = association_proxy("attribute_proxy", "description")
Attribute.published = association_proxy("attribute_proxy", "published")
Attribute.displayName = association_proxy("attribute_proxy", "displayName")
Attribute.highIsGood = association_proxy("attribute_proxy", "highIsGood")