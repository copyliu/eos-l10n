from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import mapper, synonym

from .. import gamedata_meta
from model.types import Icon

icons_table = Table("icons", gamedata_meta, 
                    Column("iconID", Integer, primary_key = True),
                    Column("description", String),
                    Column("iconFile", String))

mapper(Icon, icons_table,
       properties = {"ID" : synonym("iconID")})