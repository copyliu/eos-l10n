from model.types import Item
from model.saveddata.effectHandlerHelpers import HandledItem
from sqlalchemy.orm import validates

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
               "level" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val