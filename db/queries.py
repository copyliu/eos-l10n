import __init__ as db
from ..types import Item
from metagroup import metatypes_table

session = db.Session()

def getVariations(item):
    if(type(item) == Item.__class__): item = item.ID
    return session.query(Item).filter(and_(Item.typeID == metatypes_table.c.typeID, metatypes_table.c.parentTypeID == i)).all()

def getItem(lookfor):
    if(type(lookfor) == str):
        return session.query(Item).filter(Item.name == lookfor).one()
    elif(type(lookfor) == int):
        return session.query(Item).filter(Item.ID == lookfor).one()
    
def searchItems(nameLike):
    #Check if the string contains * signs we need to convert to %
    if "*" in nameLike: nameLike = nameLike.replace("*", "%")
    #Check for % or _ signs, if there aren't any we'll add a % at start and another one at end
    elif not "%" in nameLike and not "_" in nameLike: nameLike = "%" + nameLike + "%"
    return session.query(Item).filter(Item.name.like(nameLike)).all()