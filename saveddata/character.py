from model.effectHandlerHelpers import HandledItem
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
    
    def filteredSkillIncrease(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.increaseItemAttr(*args, **kwargs)
                
    def filteredSkillMultiply(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.multiplyItemAttr(*args, **kwargs)
                
    def filteredSkillBoost(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.boostItemAttr(*args, **kwargs)
    
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
        

class Skill(HandledItem):
    def __init__(self):
        self.__item = None
        self.__level = None
        
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        self.__item = item
        self.itemID = item.ID if item != None else None
    
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
                if effect.runTime == runTime:
                    effect.handler(fit, runTime, "skill")
    
    @validates("characterID", "skillID", "level")
    def validator(self, key, val):
        map = {"characterID": lambda val: isinstance(val, int),
               "skillID" : lambda val: isinstance(val, int),
               "level" : lambda val: isinstance(val, int) and val >= 1 and val <= 5}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val