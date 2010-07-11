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
        self.__owner = owner
    
    def setSkill(self, skill):
        self.__skills[skill.item.ID] = skill
        
    def getSkill(self, item):
        return self.__skills[item.ID if hasattr(item, "ID") else item]
    
    def iterSkills(self):
        return self.__skills.itervalues()
    
    def increaseAllSkills(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.increaseItem(*args, **kwargs)
                
    def multiplyAllSkills(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.multiplyItem(*args, **kwargs)
                
    def boostAllSkills(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.boostItem(*args, **kwargs)
                
    def calculateModifiedAttributes(self, fit, runTime):
        for skill in self.iterSkills():
            skill.calculateModifiedAttributes(fit, runTime)
                
    @validates("ID", "name", "apiKey", "ownerID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "name" : lambda val: True,
               "apiKey" : lambda val: val == None or (isinstance(val, basestring) and len(val) == 64),
               "ownerID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val