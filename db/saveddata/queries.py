#===============================================================================
# Copyright (C) 2010  Duclos Diego
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from model.db import saveddata_session
from model.types import User, Character, Fit

def getUser(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(User).filter(User.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(User).filter(User.username == lookfor).one()

def getCharacter(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(Character).filter(Character.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(Character).filter(Character.name == lookfor).one()


def getFit(fitID):
    return saveddata_session.query(Fit).filter(Fit.ID == fitID).one()
