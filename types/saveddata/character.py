from model.types import User
from sqlalchemy.orm import validates

class Character(object):
    def __init__(self, name):
        self.name = name
        self.__owner = None
        self.__skills = {}
        self.apiKey = None
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        if owner == None or type(owner) == User:
            self.__owner = owner
        else:
            raise ValueError("User should be an owner or None, not " + type(owner))
        
    @validates("ID", "name", "apiKey", "ownerID")
    def validator(self, key, val):
        map = {"ID": lambda val: type(val) == int,
               "name" : lambda val: True,
               "apiKey" : lambda val: val == None or len(val) == 64,
               "ownerID" : lambda val: type(val) == int}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val