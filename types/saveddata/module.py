from model.types import Item
from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict
from model.types.saveddata import fit
from sqlalchemy.orm import validates
    
class Module(object):
    """An instance of this class represents a module together with its charge and modified attributes"""
    
    def __init__(self):
        self.__fit = None
        self.__item = None
        self.__charge = None
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
    
    @property
    def fit(self):
        return self.__fit
    
    @fit.setter
    def fit(self, val):
        if type(val) == fit.Fit:
            self.__fit = val
        
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        if type(item) != Item and item != None: raise ValueError("Expecting an item, got a " + str(type(item)))
        self.__item = item
        self.itemID = item.ID if item != None else None
        self.__itemModifiedAttributes.original = item.attributes
        self.__chargeModifiedAttributes.clear()
        
    @property
    def charge(self):
        return self.__charge
    
    @charge.setter
    def charge(self, charge):
        if type(charge) != Item and charge != None: raise ValueError("Expecting an item, got a " + str(type(charge)))
        if not self.isValidCharge(charge): raise ValueError("Ammo does not fit in that slot")
        self.__charge = charge
        self.ammoID = charge.ID if charge != None else None
        self.__chargeModifiedAttributes.original = charge.attributes
        self.__itemModifiedAttributes.clear()
    
    def getModifiedChargeAttr(self, key):
        if key in self.__chargeModifiedAttributes:
            return self.__chargeModifiedAttributes[key]
    
    def getModifiedItemAttr(self, key):
        if key in self.__itemModifiedAttributes:
            return self.__itemModifiedAttributes[key]
    
    def isValidCharge(self, charge):
        #Check sizes, if charge size > module volume it won't fit
        if charge == None: return True
        chargeVolume = charge.getAttribute("volume")
        moduleCapacity = self.getModifiedItemAttr("capacity")
        if chargeVolume != None and moduleCapacity != None and chargeVolume > moduleCapacity:
            return False
        
        itemChargeSize = self.getModifiedItemAttr("chargeSize")
        if itemChargeSize != None:
            chargeSize = charge.getAttribute('chargeSize')
            if itemChargeSize != chargeSize:
                return False

        chargeGroup = charge.groupID
        for i in range(5):
            itemChargeGroup = self.getModifiedItemAttr('chargeGroup' + str(i))
            if itemChargeGroup == None: continue
            if itemChargeGroup == chargeGroup: return True
        
        return False
    
    @validates("ID", "itemID", "ammoID")
    def validator(self, key, val):
        map = {"ID": lambda val: type(val) == int,
               "itemID" : lambda val: type(val) == int,
               "ammoID" : lambda val: type(val) == int}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
        
    def calculateModifiedAttributes(self):
        pass