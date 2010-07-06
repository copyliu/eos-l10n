from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict

class Booster(object):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = item.attributes
        self.__sideEffects = []
        for effect in item.effects.itervalues():
            if effect.isType("boosterSideEffect"):
                s = SideEffect()
                s.effect = effect
                s.active = False
                self.__sideEffects.append(s)
    
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
            raise ValueError("Passed item is not an implant")
        
        return int(item.attributes["boosterness"].value)
    
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self)
        for sideEffect in self.iterSideEffects():
            if sideEffect.active:
                sideEffect.effect.handler(fit, self)
                
class SideEffect(object):
    def __init__(self):
        self.__active = False
        self.__effect = None
        
    @property
    def active(self):
        return self.__active
    
    @active.setter
    def active(self, active):
        if not isinstance(active, bool):
            raise TypeError("Expecting a bool, not a " + type(active))
        
        self.__active = active
        
    @property
    def effect(self):
        return self.__effect
    
    @effect.setter
    def effect(self, effect):
        if not hasattr(effect, "handler"):
            raise TypeError("Need an effect with a handler")
        
        self.__effect = effect