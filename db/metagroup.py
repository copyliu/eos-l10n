from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relation, mapper, join, synonym
import __init__ as db
from ..types import MetaGroup, Item

metagroups_table = Table("invmetagroups", db.meta,
                         Column("metaGroupID", Integer, primary_key = True),
                         Column("metaGroupName", String))

metatypes_table = Table("invmetatypes", db.meta,
                        Column("typeID", Integer, ForeignKey("invtypes.typeID"), primary_key = True),
                        Column("parentTypeID", Integer, ForeignKey("invtypes.typeID")),
                        Column("metaGroupID", Integer, ForeignKey("invmetagroups.metaGroupID")))

mapper(MetaGroup, metagroups_table,
       properties = {"ID" : synonym("metaGroupID"),
                     "name" : synonym("metaGroupName")})