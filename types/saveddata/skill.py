from model.types import Item

from sqlalchemy.orm import validates

class Skill(object):
    def __init__(self):
        self.__skill = None
        self.__level = None
        
    @property
    def skill(self):
        return self.__skill
    
    @skill.setter
    def skill(self, skill):
        self.__skill = skill
        self.skillID = skill.ID if skill != None else None
    
    @validates("characterID", "skillID", "level")
    def validator(self, key, val):
        map = {"characterID": lambda val: isinstance(val, int),
               "skillID" : lambda val: isinstance(val, int),
               "level" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val