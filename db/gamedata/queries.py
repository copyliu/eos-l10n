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

from eos.db import gamedata_session
from eos.db.gamedata.metagroup import metatypes_table
from sqlalchemy.sql import and_, or_, select, func
from sqlalchemy.orm import join
from eos.types import Item, Category, Group, MarketGroup, AttributeInfo, MetaData, MetaGroup
from eos.db.util import processEager, processWhere
import eos.config

configVal = getattr(eos.config, "gamedataCache", None)
if configVal is True:
    def cachedQuery(amount, *keywords):
        def deco(function):
            cache = {}
            def checkAndReturn(*args, **kwargs):
                useCache = kwargs.pop("useCache", True)
                cacheKey = []
                cacheKey.extend(args)
                for keyword in keywords:
                    cacheKey.append(kwargs.get(keyword))

                cacheKey = tuple(cacheKey)
                handler = cache.get(cacheKey)
                if handler is None or not useCache:
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

itemNameMap = {}
@cachedQuery(1, "lookfor")
def getItem(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            item = gamedata_session.query(Item).get(lookfor)
        else:
            item = gamedata_session.query(Item).options(*processEager(eager)).filter(Item.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        if lookfor in itemNameMap:
            id = itemNameMap[lookfor]
            if eager is None:
                item = gamedata_session.query(Item).get(id)
            else:
                item = gamedata_session.query(Item).options(*processEager(eager)).filter(Item.ID == id).first()
        else:
            # Item names are unique, so we can use first() instead of one()
            item = gamedata_session.query(Item).options(*processEager(eager)).filter(Item.name == lookfor).first()
            itemNameMap[lookfor] = item.ID
    return item

groupNameMap = {}
@cachedQuery(1, "lookfor")
def getGroup(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            group = gamedata_session.query(Group).get(lookfor)
        else:
            group = gamedata_session.query(Group).options(*processEager(eager)).filter(Group.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        if lookfor in groupNameMap:
            id = groupNameMap[lookfor]
            if eager is None:
                group = gamedata_session.query(Group).get(id)
            else:
                group = gamedata_session.query(Group).options(*processEager(eager)).filter(Group.ID == id).first()
        else:
            # Group names are unique, so we can use first() instead of one()
            group = gamedata_session.query(Group).options(*processEager(eager)).filter(Group.name == lookfor).first()
            groupNameMap[lookfor] = group.ID
    return group

categoryNameMap = {}
@cachedQuery(1, "lookfor")
def getCategory(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            category = gamedata_session.query(Category).get(lookfor)
        else:
            category = gamedata_session.query(Category).options(*processEager(eager)).filter(Category.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        if lookfor in categoryNameMap:
            id = categoryNameMap[lookfor]
            if eager is None:
                category = gamedata_session.query(Category).get(id)
            else:
                category = gamedata_session.query(Category).options(*processEager(eager)).filter(Category.ID == id).first()
        else:
            # Category names are unique, so we can use first() instead of one()
            category = gamedata_session.query(Category).options(*processEager(eager)).filter(Category.name == lookfor).first()
            categoryNameMap[lookfor] = category.ID
    return category

metaGroupNameMap = {}
@cachedQuery(1, "lookfor")
def getMetaGroup(lookfor, eager=None):
    if isinstance(lookfor, int):
        if eager is None:
            metaGroup = gamedata_session.query(MetaGroup).get(lookfor)
        else:
            metaGroup = gamedata_session.query(MetaGroup).options(*processEager(eager)).filter(MetaGroup.ID == lookfor).first()
    elif isinstance(lookfor, basestring):
        if lookfor in metaGroupNameMap:
            id = metaGroupNameMap[lookfor]
            if eager is None:
                metaGroup = gamedata_session.query(MetaGroup).get(id)
            else:
                metaGroup = gamedata_session.query(MetaGroup).options(*processEager(eager)).filter(MetaGroup.ID == id).first()
        else:
            # MetaGroup names are unique, so we can use first() instead of one()
            metaGroup = gamedata_session.query(MetaGroup).options(*processEager(eager)).filter(MetaGroup.name == lookfor).first()
            metaGroupNameMap[lookfor] = metaGroup.ID
    return metaGroup

@cachedQuery(1, "lookfor")
def getMarketGroup(lookfor, eager=None):
    if eager is None:
        marketGroup = gamedata_session.query(MarketGroup).get(lookfor)
    else:
        marketGroup = gamedata_session.query(MarketGroup).options(*processEager(eager)).filter(MarketGroup.ID == lookfor).first()
    return marketGroup

@cachedQuery(2, "where", "filter")
def getItemsByCategory(filter, where=None, eager=None):
    if isinstance(filter, int):
        filter = Category.ID == filter
    elif isinstance(filter, basestring):
        filter = Category.name == filter

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

    filter = processWhere(func.lower(Item.name).like(nameLike.lower()), where)
    return gamedata_session.query(Item).options(*processEager(eager)).join(*join).filter(filter).all()

@cachedQuery(3, "where", "item", "metaGroups")
def getVariations(item, where=None, metaGroups=None, eager=None):
    if not isinstance(item, int):
        item = item.ID

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

@cachedQuery(1, "attr")
def getAttributeInfo(attr, eager=None):
    if isinstance(attr, basestring):
        filter = AttributeInfo.name == attr
    elif isinstance(attr, int):
        filter = AttributeInfo.ID == attr

    return gamedata_session.query(AttributeInfo).options(*processEager(eager)).filter(filter).one()

@cachedQuery(1, "field")
def getMetaData(field):
    return gamedata_session.query(MetaData).filter(MetaData.fieldName == field).one()

@cachedQuery(2, "itemIDs", "attributeID")
def directAttributeRequest(itemIDs, attrID):
    q = select((eos.types.Item.ID, eos.types.Attribute.value),
                                  and_(eos.types.Attribute.attributeID == attrID, eos.types.Item.ID.in_(itemIDs)),
                                  from_obj=[join(eos.types.Attribute, eos.types.Item)])

    return gamedata_session.execute(q).fetchall()
