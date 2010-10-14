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

from eos.db import gamedata_session
from eos.db.gamedata.metagroup import metatypes_table
from sqlalchemy.sql import and_, or_
from eos.types import Item, Category, Group, MarketGroup, AttributeInfo
from eos.db.util import processEager, processWhere
import eos.config

configVal = getattr(eos.config, "gamedataCache", None)
if configVal is True:
    def cachedQuery(amount, *keywords):
        def deco(function):
            cache = {}
            def checkAndReturn(*args, **kwargs):
                cacheKey = []
                cacheKey.extend(args)
                for keyword in keywords:
                    cacheKey.append(kwargs.get(keyword))

                cacheKey = tuple(cacheKey)
                handler = cache.get(cacheKey)
                if handler is None:
                    handler = cache[cacheKey] = function(*args, **kwargs)

                return handler

            return checkAndReturn
        return deco

elif callable(configVal):
    cachedQuery = eos.config.gamedataCache
else:
    def cachedQuery(amount, *keywords):
        def deco(function):
            def checkAndReturn(*args, **kwargs):
                return function(*args, **kwargs)

            return checkAndReturn
        return deco

@cachedQuery(1, "lookfor")
def getItem(lookfor, eager=None):
    if isinstance(lookfor, basestring):
        return gamedata_session.query(Item).options(*processEager(eager)).filter(Item.name == lookfor).one()
    elif isinstance(lookfor, (int, float)):
        return gamedata_session.query(Item).options(*processEager(eager)).filter(Item.ID == int(lookfor)).one()

@cachedQuery(2, "where", "filter")
def getItemsByCategory(filter, where=None, eager=None):
    if isinstance(filter, basestring):
        filter = Category.name == filter
    elif isinstance(filter, (int, float)):
        filter = Category.ID == int(filter)

    filter = processWhere(filter, where)
    return gamedata_session.query(Item).options(*processEager(eager)).join(Item.group, Group.category).filter(filter).all()

@cachedQuery(3, "where", "nameLike", "join")
def searchItems(nameLike, where=None, join=None, eager=None):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%%%s%%" % nameLike

    if join is None:
        join = tuple()

    if not hasattr(join, "__iter__"):
        join = (join,)

    filter = processWhere(Item.name.like(nameLike), where)
    return gamedata_session.query(Item).options(*processEager(eager)).join(*join).filter(filter).all()

@cachedQuery(3, "where", "item", "metaGroups")
def getVariations(item, where=None, metaGroups=None, eager=None):
    if not isinstance(item, (int, float)):
        item = item.ID
    else:
        item = int(item)

    clause = and_(Item.typeID == metatypes_table.c.typeID, metatypes_table.c.parentTypeID == item)

    if metaGroups != None:
        if not hasattr(metaGroups, "__iter__"):
            metaGroups = (metaGroups,)

        metaClause = metatypes_table.c.metaGroupID == metaGroups[0]
        i = 1
        while i < len(metaGroups):
            metaClause = or_(metaClause, metatypes_table.c.metaGroupID == metaGroups[i])
            i += 1

        clause = and_(clause, metaClause)


    filter = processWhere(clause, where)
    return gamedata_session.query(Item).options(*processEager(eager)).filter(filter).all()

@cachedQuery(1, "group")
def getGroup(group, eager=None):
    if isinstance(group, basestring):
        filter = Group.name == group
    elif isinstance(group, (int, float)):
        filter = Group.ID == int(group)

    return gamedata_session.query(Group).options(*processEager(eager)).filter(filter).one()

@cachedQuery(1, "category")
def getCategory(category, eager=None):
    if isinstance(category, basestring):
        filter = Category.name == category
    elif isinstance(category, (int, float)):
        filter = Category.ID == int(category)

    return gamedata_session.query(Category).options(*processEager(eager)).filter(filter).one()

@cachedQuery(1, "group")
def getMarketGroup(group, eager=None):
    if isinstance(group, basestring):
        filter = MarketGroup.name == group
    elif isinstance(group, (int, float)):
        filter = MarketGroup.ID == int(group)

    return gamedata_session.query(MarketGroup).options(*processEager(eager)).filter(filter).one()

@cachedQuery(1, "attr")
def getAttributeInfo(attr, eager=None):
    if isinstance(attr, basestring):
        filter = AttributeInfo.name == attr
    elif isinstance(attr, (int, float)):
        filter = AttributeInfo.ID == int(attr)

    return gamedata_session.query(AttributeInfo).options(*processEager(eager)).filter(filter).one()
