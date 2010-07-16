from model.types import Item
from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut, ChargeAttrShortcut
from model.effectHandlerHelpers import HandledItem, HandledCharge
from sqlalchemy.orm import validates, reconstructor
class Drone(HandledItem, HandledCharge, ItemAttrShortcut, ChargeAttrShortcut):
    def __init__(self, item):
        if item.category.name != "Drone":
            raise ValueError("Passed item is not a drone")
        
        self.__item = item
        self.itemID = item.ID
        self.amount = 0
        self.build()
        
    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.build()
        
    def build(self):
        from model import db
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
        self.itemModifiedAttributes.original = self.item.attributes
        chargeID = self.getModifiedItemAttr("entityMissileTypeID")
        if chargeID != None:
            charge = db.getItem(int(chargeID))
            self.__charge = charge
            self.chargeModifiedAttributes.original = charge.attributes
    
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    @property
    def chargeModifiedAttributes(self):
        return self.__chargeModifiedAttributes
    
    @property
    def item(self):
        return self.__item
        
    @property
    def charge(self):
        return self.__charge
    
    @validates("ID", "itemID", "chargeID", "amount")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "chargeID" : lambda val: isinstance(val, int),
               "amount" : lambda val: isinstance(val, int) and val >= 0}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
    
    def clear(self):
        self.itemModifiedAttributes.clear()
        self.chargeModifiedAttributes.clear()
        
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self, "drone")
        for effect in self.charge.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self, "droneCharge")