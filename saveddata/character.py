from model.effectHandlerHelpers import HandledItem
from sqlalchemy.orm import validates, reconstructor

class Character(object):
    def __init__(self, name):
        self.name = name
        self.__owner = None
        self.__skills = set()
        self.apiKey = None
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        self.__owner = owner
    
    def addSkill(self, skill):
        self.__skills.add(skill)
        
    def getSkill(self, item):
        for skill in self.__skills:
            if skill.item.ID == item or skill.item == item or skill.item.name == item:
                return skill
            
    def iterSkills(self):
        return self.__skills.__iter__()
    
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
    
    def clear(self):
        for skill in self.iterSkills():
            skill.clear()
            
    @validates("ID", "name", "apiKey", "ownerID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "name" : lambda val: True,
               "apiKey" : lambda val: val == None or (isinstance(val, basestring) and len(val) == 64),
               "ownerID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
        

class Skill(HandledItem):
    def __init__(self, item, level = 0):
        self.__item = item
        self.itemID = item.ID
        self.level = level
        self.build()
    
    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.build()
        
    def build(self):
        self.__suppressed = False
        
    @property
    def item(self):
        return self.__item
    
    def calculateModifiedAttributes(self, fit, runTime):
        if self.__suppressed: return
        for effect in self.item.effects:
                if effect.runTime == runTime:
                    effect.handler(fit, runTime, "skill")
    
    def clear(self):
        self.__suppressed = False
    
    def suppress(self):
        self.__suppressed = True
    
    def isSuppressed(self):
        return self.__suppressed
    
    @validates("characterID", "skillID", "level")
    def validator(self, key, val):
        map = {"characterID": lambda val: isinstance(val, int),
               "skillID" : lambda val: isinstance(val, int),
               "level" : lambda val: isinstance(val, int) and val >= 0 and val <= 5}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val