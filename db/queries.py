from __init__ import gamedata_session
from ..types import Item
from gamedata.metagroup import metatypes_table
from sqlalchemy.sql import and_

def getItem(lookfor):
    if type(lookfor) == str:
        return gamedata_session.query(Item).filter(Item.name == lookfor).one()
    elif type(lookfor) == int:
        return gamedata_session.query(Item).filter(Item.ID == lookfor).one()
    
def searchItems(nameLike):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%" + nameLike + "%"
    return gamedata_session.query(Item).filter(Item.name.like(nameLike)).all()

def getVariations(item):
    if type(item) == Item: item = item.ID
    return gamedata_session.query(Item).filter(and_(Item.typeID == metatypes_table.c.typeID, metatypes_table.c.parentTypeID == item)).all()