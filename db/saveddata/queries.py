from model.db import saveddata_session
from model.types import User, Character

def getUser(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(User).filter(User.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(User).filter(User.username == lookfor).one()

def getCharacter(lookfor):
    if isinstance(lookfor, int): return saveddata_session.query(Character).filter(Character.ID == lookfor).one()
    elif isinstance(lookfor, basestring): return saveddata_session.query(Character).filter(Character.name == lookfor).one()