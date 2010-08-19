#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy import MetaData,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from eos import config

class ReadOnlyException(Exception):
    pass

#Method to replace flush with for read-only sessions
def abort_ro():
    raise ReadOnlyException()

gamedata_engine = create_engine(config.gamedata_connectionstring, echo = config.debug)
gamedata_meta = MetaData()
gamedata_meta.bind = gamedata_engine
gamedata_session = sessionmaker(bind=gamedata_engine, autoflush = False)()
#Make gamedata_session read only
gamedata_session.flush = abort_ro

saveddata_engine = create_engine(config.saveddata_connectionstring, echo = config.debug)
saveddata_meta = MetaData()
saveddata_meta.bind = saveddata_engine
saveddata_session = sessionmaker(bind=saveddata_engine, autoflush = False)()

#Import all the definitions for all our database stuff
from .gamedata import *
from .saveddata import *

#Import queries
from .gamedata.queries import getItem, searchItems, getVariations, getItemsByCategory, getMarketGroup, getGroup, getCategory
from .saveddata.queries import getUser, getCharacter, getFit
