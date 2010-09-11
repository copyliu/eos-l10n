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

from eos.db.util import processEager, processWhere
from eos.db import saveddata_session
from eos.types import User, Character, Fit, Price
from sqlalchemy.sql import and_

def getUser(lookfor, where=None, eager=None):
    if isinstance(lookfor, int):
        return saveddata_session.query(User).options(*processEager(eager)).filter(User.ID == lookfor).one()
    elif isinstance(lookfor, basestring):
        return saveddata_session.query(User).options(*processEager(eager)).filter(User.username == lookfor).one()

def getCharacter(lookfor, where=None, eager=None):
    if isinstance(lookfor, int):
        return saveddata_session.query(Character).options(*processEager(eager)).filter(Character.ID == lookfor).one()
    elif isinstance(lookfor, basestring):
        return saveddata_session.query(Character).options(*processEager(eager)).filter(Character.name == lookfor).one()

def getCharacterList(eager=None):
    return saveddata_session.query(Character).all()

def getFit(fitID, where=None, eager=None):
    return saveddata_session.query(Fit).options(*processEager(eager)).filter(Fit.ID == fitID).one()

def getFitsWithShip(shipID, ownerID=None, where=None, eager=None):
    """
    Get all the fits using a certain ship.
    If no user is passed, do this for all users.
    """
    filter = Fit.shipID == shipID
    if ownerID is not None:
        filter = _and(filter, Fit.ownerID == ownerID)

    filter = processWhere(filter, where)
    return saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).all()

def getPrice(typeID):
    return saveddata_session.query(Price).filter(Price.typeID == typeID)

def searchFits(nameLike, where=None, eager=None):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%%%s%%" % nameLike

    #Add any extra components to the search to our where clause
    filter = processWhere(Fit.name.like(nameLike), where)
    return saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).all()

def save(stuff):
    saveddata_session.add(stuff)
    commit()

def remove(stuff):
    saveddata_session.delete(stuff)
    commit()

def commit():
    saveddata_session.commit()
    saveddata_session.flush()
