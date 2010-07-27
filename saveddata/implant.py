from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut
from model.effectHandlerHelpers import HandledItem
from sqlalchemy.orm import validates, reconstructor
class Implant(HandledItem, ItemAttrShortcut):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.itemID = item.ID
        self.build()
    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.__slot = self.__calculateSlot(self.__item)
        self.build()
        
    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.item.attributes
    
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    @property
    def slot(self):
        return self.__slot
    
    @property
    def item(self):
        return self.__item

    def __calculateSlot(self, item):
        if not "implantness" in item.attributes:
            raise ValueError("Passed item is not an implant")
        
        return int(item.attributes["implantness"].value)
    
    def clear(self):
        self.itemModifiedAttributes.clear()
        
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime:
                effect.handler(fit, self, "implant")
                
    @validates("fitID", "itemID")
    def validator(self, key, val):
        map = {"fitID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
        