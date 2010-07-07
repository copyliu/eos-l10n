from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict

from sqlalchemy.orm import reconstructor, validates

class Booster(object):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.itemID = item.ID
        self.__item = item
        self.build()
        
    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.__slot = self.__calculateSlot(self.__item)
        self.build()
        
    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.__item.attributes
        self.__sideEffects = []
        for effect in self.item.effects.itervalues():
            if effect.isType("boosterSideEffect"):
                s = SideEffect(self)
                s.effect = effect
                s.active = effect.ID in self.__activeSideEffectIDs
                self.__sideEffects.append(s)
    
    def iterSideEffects(self):
        return self.__sideEffects.__iter__()
    
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    @property
    def slot(self):
        return self.__slot
    
    @property
    def item(self):
        return self.__item
    
    def iterSideEffects(self):
        return self.__sideEffects.__iter__()
    
    def __calculateSlot(self, item):
        if not "boosterness" in item.attributes:
            raise ValueError("Passed item is not a booster")
        
        return int(item.attributes["boosterness"].value)
    
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self)
        for sideEffect in self.iterSideEffects():
            if sideEffect.active:
                sideEffect.effect.handler(fit, self)
                
    @validates("ID", "itemID", "ammoID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
                
class SideEffect(object):
    def __init__(self, owner):
        self.__owner = owner
        self.__active = False
        self.__effect = None
        
    @property
    def active(self):
        return self.__active
    
    @active.setter
    def active(self, active):
        if not isinstance(active, bool):
            raise TypeError("Expecting a bool, not a " + type(active))
        
        if active != self.__active:
            if active:
                self.__owner._Booster__activeSideEffectIDs.append(self.effect.ID)
            else:
                self.__owner._Booster__activeSideEffectIDs.remove(self.effect.ID)
            
            self.__active = active
        
    @property
    def effect(self):
        return self.__effect
    
    @effect.setter
    def effect(self, effect):
        if not hasattr(effect, "handler"):
            raise TypeError("Need an effect with a handler")
        
        self.__effect = effect