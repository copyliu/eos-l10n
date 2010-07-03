from model.types import User

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
            self.ownerID = None if owner == None else owner.ID
        else:
            raise ValueError("User should be an owner or None, not " + type(owner))