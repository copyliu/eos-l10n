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

from eos.db import saveddata_session
from eos.types import User, Character, Fit
from sqlalchemy.sql import and_

def getUser(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(User).filter(User.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(User).filter(User.username == lookfor).one()

def getCharacter(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(Character).filter(Character.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(Character).filter(Character.name == lookfor).one()


def getFit(fitID):
    return saveddata_session.query(Fit).filter(Fit.ID == fitID).one()

def getFitsWithShip(shipID, ownerID=None):
    """
    Get all the fits using a certain ship.
    If no user is passed, do this for all users.
    """
    filter = Fit.shipID == shipID
    if ownerID is not None:
        filter = _and(filter, Fit.ownerID == ownerID)

    return saveddata_session.query(Fit).filter(filter).all()
