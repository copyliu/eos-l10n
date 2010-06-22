from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import mapper

import __init__ as db
from ..types import Icon

icons_table = Table("icons", db.meta, 
                    Column("iconID", Integer, primary_key = True),
                    Column("description", String),
                    Column("iconFile", String))

mapper(Icon, icons_table)