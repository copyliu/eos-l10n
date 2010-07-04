from model.db import saveddata_session
from model.types import User, Character

def getUser(lookfor):
    if type(lookfor) == int: return saveddata_session.query(User).filter(User.ID == lookfor).one()
    elif type(lookfor) == str: return saveddata_session.query(User).filter(User.username == lookfor).one()

def getCharacter(lookfor):
    if type(lookfor) == int: return saveddata_session.query(Character).filter(Character.ID == lookfor).one()
    elif type(lookfor) == str: return saveddata_session.query(Character).filter(Character.name == lookfor).one()