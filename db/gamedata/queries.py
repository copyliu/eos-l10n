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

from eos.db import gamedata_session
from eos.db.gamedata.metagroup import metatypes_table
from sqlalchemy.sql import and_
from eos.types import Item, Category, Group, MarketGroup
from eos.db.queryCache import cachedQuery
from sqlalchemy.orm import eagerload

def processEager(eager):
    if eager == None:
        return tuple()
    else:
        l = []
        if isinstance(eager, basestring):
            eager = (eager,)

        for e in eager:
            l.append(eagerload(e))

        return l

@cachedQuery
def getItem(lookfor, eager=None):
    if isinstance(lookfor, basestring):
        return gamedata_session.query(Item).options(*processEager(eager)).filter(Item.name == lookfor).one()
    elif isinstance(lookfor, int):
        return gamedata_session.query(Item).options(*processEager(eager)).filter(Item.ID == lookfor).one()

@cachedQuery
def getItemsByCategory(filter, eager=None):
    if isinstance(filter, basestring):
        filter = Category.name == filter
    elif isinstance(filter, int):
        filter = Category.ID == filter

    return gamedata_session.query(Item).options(*processEager(eager)).join(Item.group, Group.category).filter(filter).all()

@cachedQuery
def searchItems(nameLike, eager=None):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%%%s%%" % nameLike
    return gamedata_session.query(Item).options(*processEager(eager)).filter(Item.name.like(nameLike)).all()

@cachedQuery
def getVariations(item, eager=None):
    if not isinstance(item, int): item = item.ID
    return gamedata_session.query(Item).options(*processEager(eager)).filter(and_(Item.typeID == metatypes_table.c.typeID, metatypes_table.c.parentTypeID == item)).all()

@cachedQuery
def getGroup(group, eager=None):
    if isinstance(group, basestring):
        filter = Group.name == group
    elif isinstance(group, int):
        filter = Group.ID == group

    return gamedata_session.query(Group).options(*processEager(eager)).filter(filter).one()

@cachedQuery
def getCategory(category, eager=None):
    if isinstance(category, basestring):
        filter = Category.name == category
    elif isinstance(category, int):
        filter = Category.ID == category

    return gamedata_session.query(Category).options(*processEager(eager)).filter(filter).one()

@cachedQuery
def getMarketGroup(group, eager=None):
    if isinstance(group, basestring):
        filter = MarketGroup.name == group
    elif isinstance(group, int):
        filter = MarketGroup.ID == group

    return gamedata_session.query(MarketGroup).options(*processEager(eager)).filter(filter).one()
