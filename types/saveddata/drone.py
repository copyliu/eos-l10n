from model.types import Item
from model.types.saveddata.module import ModifiedAttributeDict

from sqlalchemy.orm import validates, reconstructor

class Drone(object):
    def __init__(self):
        self.amount = 0
        self.__item = None
        self.__charge = None
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
        
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    @property
    def chargeModifiedAttributes(self):
        return self.__chargeModifiedAttributes
    
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        if item.category.name != "Drone":
            print item.category
            raise ValueError("Passed item is not a drone")
        self.__item = item
        
    @property
    def charge(self):
        return self.__charge
    
    @charge.setter
    def charge(self, charge):
        print self.item.attributes["entityMissileTypeID"].value, charge.ID, self.getModifiedItemAttr("entityMissileTypeID")
        if charge.ID != self.getModifiedItemAttr("entityMissileTypeID"):
            raise ValueError("Charge does not fit on this drone")
        
        self.__charge = charge
        
    def getModifiedItemAttr(self, key):
        if key in self.itemModifiedAttributes:
            return self.itemModifiedAttributes[key]
        else:
            return None
        
    def getModifiedAmmoAttr(self, key):
        if key in self.ammoModifiedAttributes:
            return self.ammoModifiedAttributes[key]
        else:
            return None
        
    @validates
    def validator(self, key, val):
        if key == "ID": return isinstance(val, int)