#===============================================================================
# Copyright (C) 2010 Diego Duclos
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

from model.db import gamedata_session
from model.db.gamedata.metagroup import metatypes_table
from sqlalchemy.sql import and_
from model.types import Item, Category, Group, MarketGroup
def getItem(lookfor):
    if isinstance(lookfor, basestring):
        return gamedata_session.query(Item).filter(Item.name == lookfor).one()
    elif isinstance(lookfor, int):
        return gamedata_session.query(Item).filter(Item.ID == lookfor).one()

def getItemsByCategory(filter):
    if isinstance(filter, basestring):
        filter = Category.name == filter
    elif isinstance(filter, int):
        filter = Category.ID == filter

    return gamedata_session.query(Item).join(Item.group, Group.category).filter(filter).all()

def searchItems(nameLike):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%" + nameLike + "%"
    return gamedata_session.query(Item).filter(Item.name.like(nameLike)).all()

def getVariations(item):
    if not isinstance(item, int): item = item.ID
    return gamedata_session.query(Item).filter(and_(Item.typeID == metatypes_table.c.typeID, metatypes_table.c.parentTypeID == item)).all()

def getGroup(group):
    if isinstance(group, basestring):
        filter = Group.name == group
    elif isinstance(group, int):
        filter = Group.ID == group

    return gamedata_session.query(Group).filter(filter).one()

def getMarketGroup(group):
    if isinstance(group, basestring):
        filter = MarketGroup.name == group
    elif isinstance(group, int):
        filter = MarketGroup.ID == group

    return gamedata_session.query(MarketGroup).filter(filter).one()
