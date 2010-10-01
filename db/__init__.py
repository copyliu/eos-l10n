#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import pool
from eos import config

class ReadOnlyException(Exception):
    pass

gamedata_engine = create_engine(config.gamedata_connectionstring,
                                echo = config.debug)
gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine
gamedata_session = scoped_session(sessionmaker(bind=gamedata_engine, autoflush=False, expire_on_commit=False))

if config.saveddata_connectionstring is not None:
    saveddata_engine = create_engine(config.saveddata_connectionstring, echo=config.debug, poolclass=pool.StaticPool)
    saveddata_meta = MetaData()
    saveddata_meta.bind = saveddata_engine
    saveddata_session = scoped_session(sessionmaker(bind=saveddata_engine, autoflush=False, expire_on_commit=False))


#Import all the definitions for all our database stuff
from eos.db.gamedata import *
from eos.db.saveddata import *

#Import queries
from eos.db.gamedata.queries import getItem, searchItems, getVariations, getItemsByCategory, getMarketGroup, getGroup, getCategory, getAttributeInfo
from eos.db.saveddata.queries import getUser, getCharacter, getFit, getFitsWithShip, searchFits, getCharacterList, getPrice, getDamagePatternList, save, remove, commit

#If using in memory saveddata, you'll want to reflect it so the data structure is good.
if config.saveddata_connectionstring == "sqlite:///:memory:":
    saveddata_meta.create_all()
