#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
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
from eos.types import User, Character, Fit, Price, DamagePattern, Fleet
from sqlalchemy.sql import and_
import eos.config

configVal = getattr(eos.config, "saveddataCache", None)
if configVal is True:
    import weakref
    itemCache = {}
    queryCache = {}
    def cachedQuery(type, amount, *keywords):
        itemCache[type] = localItemCache = weakref.WeakValueDictionary()
        queryCache[type] = typeQueryCache = {}
        def deco(function):
            localQueryCache = typeQueryCache[function] = {}
            def setCache(cacheKey, args, kwargs):
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

                return items

            def checkAndReturn(*args, **kwargs):
                useCache = kwargs.pop("useCache", True)
                cacheKey = []
                cacheKey.extend(args)
                for keyword in keywords:
                    cacheKey.append(kwargs.get(keyword))

                cacheKey = tuple(cacheKey)
                info = localQueryCache.get(cacheKey)
                if info is None or not useCache:
                    items = setCache(cacheKey, args, kwargs)
                else:
                    l, IDs = info
                    if l:
                        items = []
                        for ID in IDs:
                            data = localItemCache.get(ID)
                            if data is None:
                                #Fuck, some of our stuff isn't cached it seems.
                                items = setCache(cacheKey, args, kwargs)
                                break
                            items.append(data)
                    else:
                        for ID in IDs:
                            items = localItemCache.get(ID)
                            if items is None:
                                items = setCache(cacheKey, args, kwargs)
                            break

                return items
            return checkAndReturn
        return deco

    def removeCachedEntry(type, ID):
        functionCache = queryCache[type]
        for _, localCache in functionCache.iteritems():
            toDelete = set()
            for cacheKey, info in localCache.iteritems():
                IDs = info[1]
                if ID in IDs:
                    toDelete.add(cacheKey)

            for cacheKey in toDelete:
                del localCache[cacheKey]

            if ID in itemCache[type]:
                del itemCache[type][ID]

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

@cachedQuery(User, 1, "lookfor")
def getUser(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            user = saveddata_session.query(User).get(lookfor)
        else:
            user = saveddata_session.query(User).options(*processEager(eager)).filter(User.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        user = saveddata_session.query(User).options(*processEager(eager)).filter(User.username == lookfor).first()
    else:
        raise TypeError("Need integer or string as argument")
    return user

@cachedQuery(Character, 1, "lookfor")
def getCharacter(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            character = saveddata_session.query(Character).get(lookfor)
        else:
            character = saveddata_session.query(Character).options(*processEager(eager)).filter(Character.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        character = saveddata_session.query(Character).options(*processEager(eager)).filter(Character.name == lookfor).first()
    else:
        raise TypeError("Need integer or string as argument")
    return character

def getCharacterList(eager=None):
    characters = saveddata_session.query(Character).options(*processEager(eager)).all()
    return characters

def getCharactersForUser(lookfor, eager=None):
    if isinstance(lookfor, int):
        characters = saveddata_session.query(Character).options(*processEager(eager)).filter(Character.ownerID == lookfor).all()
    else:
        raise TypeError("Need integer as argument")
    return characters

@cachedQuery(Fit, 1, "lookfor")
def getFit(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            fit = saveddata_session.query(Fit).get(lookfor)
        else:
            fit = saveddata_session.query(Fit).options(*processEager(eager)).filter(Fit.ID == fitID).first()
    else:
        raise TypeError("Need integer as argument")
    return fit

@cachedQuery(Fleet, 1, "lookfor")
def getFleet(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            fleet = saveddata_session.query(Fleet).get(lookfor)
        else:
            fleet = saveddata_session.query(Fleet).options(*processEager(eager)).filter(Fleet.ID == fleetID).one()
    else:
        raise TypeError("Need integer as argument")
    return fleet

def getFitsWithShip(shipID, ownerID=None, where=None, eager=None):
    """
    Get all the fits using a certain ship.
    If no user is passed, do this for all users.
    """
    if isinstance(shipID, int):
        if ownerID is not None and not isinstance(ownerID, int):
            raise TypeError("OwnerID must be integer")
        filter = Fit.shipID == shipID
        if ownerID is not None:
            filter = and_(filter, Fit.ownerID == ownerID)

        filter = processWhere(filter, where)
        fits = saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).all()
    else:
        raise TypeError("ShipID must be integer")
    return fits

def countFitsWithShip(shipID, ownerID=None, where=None, eager=None):
    """
    Get all the fits using a certain ship.
    If no user is passed, do this for all users.
    """
    if isinstance(shipID, int):
        if ownerID is not None and not isinstance(ownerID, int):
            raise TypeError("OwnerID must be integer")
        filter = Fit.shipID == shipID
        if ownerID is not None:
            filter = and_(filter, Fit.ownerID == ownerID)

        filter = processWhere(filter, where)
        count = saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).count()
    else:
        raise TypeError("ShipID must be integer")
    return count

def getFitList(eager=None):
    fits = saveddata_session.query(Fit).options(*processEager(eager)).all()
    return fits

def getFleetList(eager=None):
    fleets = saveddata_session.query(Fleet).options(*processEager(eager)).all()
    return fleets

@cachedQuery(Price, 1, "typeID")
def getPrice(typeID):
    if isinstance(typeID, int):
        price = saveddata_session.query(Price).get(typeID)
    else:
        raise TypeError("Need integer as argument")
    return price

def getDamagePatternList(eager=None):
    patterns = saveddata_session.query(DamagePattern).options(*processEager(eager)).all()
    return patterns

@cachedQuery(DamagePattern, 1, "lookfor")
def getDamagePattern(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            pattern = saveddata_session.query(DamagePattern).get(lookfor)
        else:
            pattern = saveddata_session.query(DamagePattern).options(*processEager(eager)).filter(DamagePattern.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        pattern = saveddata_session.query(DamagePattern).options(*processEager(eager)).filter(DamagePattern.name == lookfor).first()
    else:
        raise TypeError("Need integer or string as argument")
    return pattern

def searchFits(nameLike, where=None, eager=None):
    if not isinstance(nameLike, basestring):
        raise TypeError("Need string as argument")
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%%%s%%" % nameLike

    #Add any extra components to the search to our where clause
    filter = processWhere(Fit.name.like(nameLike), where)
    fits = saveddata_session.query(Fit).options(*processEager(eager)).filter(filter).all()
    return fits

def add(stuff):
    saveddata_session.add(stuff)

def save(stuff):
    add(stuff)
    commit()

def remove(stuff):
    removeCachedEntry(type(stuff), stuff.ID)
    saveddata_session.delete(stuff)
    commit()

def commit():
    saveddata_session.commit()
    saveddata_session.flush()
