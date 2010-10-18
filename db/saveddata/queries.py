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
from eos.types import User, Character, Fit, Price, DamagePattern
from sqlalchemy.sql import and_
from sqlalchemy.orm import make_transient
from sqlalchemy.exc import InvalidRequestError
import eos.config

configVal = getattr(eos.config, "saveddataCache", None)
if configVal is True:
    itemCache = {}
    queryCache = {}
    def cachedQuery(type, amount, *keywords):
        itemCache[type] = localItemCache = {}
        queryCache[type] = typeQueryCache = {}
        def deco(function):
            localQueryCache = typeQueryCache[type] = {}
            def checkAndReturn(*args, **kwargs):
                cacheKey = []
                cacheKey.extend(args)
                for keyword in keywords:
                    cacheKey.append(kwargs.get(keyword))

                cacheKey = tuple(cacheKey)
                info = localQueryCache.get(cacheKey)
                if info is None:
                    items = function(*args, **kwargs)
                    IDs = set()
                    localQueryCache[cacheKey] = (isinstance(items, list), IDs)
                    stuff = items if isinstance(items, list) else (items,)
                    for item in stuff:
                        ID = getattr(item, "ID", None)
                        if ID is None:
                            #Some uncachable data, don't cache this query
                            del localQueryCache[cacheKey]
                            break
                        localItemCache[ID] = item
                        IDs.add(ID)
                else:
                    l, IDs = info
                    if l:
                        items = []
                        for ID in IDs:
                            items.append(localItemCache[ID])
                    else:
                        for ID in IDs:
                            items = localItemCache[ID]
                            break

                return items
            return checkAndReturn
        return deco

    def removeCachedEntry(type, ID):
        localCache = queryCache[type]
        for cacheKey, IDs in localCache.iteritems():
            if ID in IDs:
                del localCache[cacheKey]

elif callable(configVal):
    cachedQuery, removeCachedEntry = eos.config.gamedataCache
else:
    def cachedQuery(amount, *keywords):
        def deco(function):
            def checkAndReturn(*args, **kwargs):
                return function(*args, **kwargs)

            return checkAndReturn
        return deco

    def removeCachedEntry(*args, **kwargs):
        return

@cachedQuery(User, 2, "lookfor", "where")
def getUser(lookfor, where=None, eager=None):
    if isinstance(lookfor, int):
        return saveddata_session.query(User).options(*processEager(eager)).filter(User.ID == lookfor).one()
    elif isinstance(lookfor, basestring):
        return saveddata_session.query(User).options(*processEager(eager)).filter(User.username == lookfor).one()

@cachedQuery(Character, 2, "lookfor", "where")
def getCharacter(lookfor, where=None, eager=None):
    if isinstance(lookfor, int):
        return saveddata_session.query(Character).options(*processEager(eager)).filter(Character.ID == lookfor).one()
    elif isinstance(lookfor, basestring):
        return saveddata_session.query(Character).options(*processEager(eager)).filter(Character.name == lookfor).one()

def getCharacterList(eager=None):
    return saveddata_session.query(Character).options(*processEager(eager)).all()

@cachedQuery(Fit, 2, "fitID", "where")
def getFit(fitID, where=None, eager=None):
    return saveddata_session.query(Fit).options(*processEager(eager)).filter(Fit.ID == fitID).one()

def getFitsWithShip(shipID, ownerID=None, where=None, eager=None):
    """
    Get all the fits using a certain ship.
    If no user is passed, do this for all users.
    """
    filter = Fit.shipID == shipID
    if ownerID is not None:
        filter = and_(filter, Fit.ownerID == ownerID)

    filter = processWhere(filter, where)
    return saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).all()

@cachedQuery(Price, 1, "typeID")
def getPrice(typeID):
    return saveddata_session.query(Price).filter(Price.typeID == typeID).one()

def getDamagePatternList(eager=None):
    return saveddata_session.query(DamagePattern).options(*processEager(eager)).all()

@cachedQuery(DamagePattern, 1, "lookfor")
def getDamagePattern(lookfor, eager=None):
    if isinstance(lookfor, int):
        filter = DamagePattern.ID == lookfor
    elif isinstance(lookfor, basestring):
        filter = DamagePattern.name == lookfor

    return saveddata_session.query(DamagePattern).options(*processEager(eager)).filter(filter).one()

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
    removeCachedEntry(type(stuff), stuff.ID)
    saveddata_session.delete(stuff)
    saveddata_session.expunge(stuff)
    commit()

def commit():
    saveddata_session.commit()
    saveddata_session.flush()
