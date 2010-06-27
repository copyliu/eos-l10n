from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relation, mapper, synonym

from .. import gamedata_meta
from model.types import Item, MarketGroup, Icon

marketgroups_table = Table("invmarketgroups", gamedata_meta,
                           Column("marketGroupID", Integer, primary_key = True),
                           Column("marketGroupName", String),
                           Column("description", String),
                           Column("hasTypes", Boolean),
                           Column("parentGroupID", Integer, ForeignKey("invmarketgroups.marketGroupID")),
                           Column("iconID", Integer, ForeignKey("icons.iconID")))

mapper(MarketGroup, marketgroups_table,
       properties = {"items" : relation(Item, backref = "marketGroup"),
                     "parent" : relation(MarketGroup, backref = "children", remote_side = [marketgroups_table.c.marketGroupID]),
                     "icon" : relation(Icon),
                     "ID" : synonym("marketGroupID"),
                     "name" : synonym("marketGroupName")})