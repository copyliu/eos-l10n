from model.types import Item
from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor

class State():
    OFFLINE = -1
    ONLINE = 0
    ACTIVE = 1
    OVERHEATED = 2
    
class Slot():
    LOW = 1
    MED = 2
    HIGH = 3
    DRONE = 4
    
class Module(object):
    """An instance of this class represents a module together with its charge and modified attributes"""
    
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.itemID = item.ID if item != None else None
        self.__charge = None
        self.build()
    
    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.__charge = db.getItem(self.chargeID) if self.chargeID != None else None
        
        self.build()
    
    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.item.attributes
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
        if self.charge != None:
            self.__chargeModifiedAttributes.original = self.charge.attributes
    
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
    
    @charge.setter
    def charge(self, charge):
        if not self.isValidCharge(charge): raise ValueError("Ammo does not fit in that slot")
        self.__charge = charge
        self.chargeID = charge.ID if charge != None else None
        self.__chargeModifiedAttributes.original = charge.attributes
        self.__itemModifiedAttributes.clear()
    
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
        
    def isValidCharge(self, charge):
        #Check sizes, if 'charge size > module volume' it won't fit
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
    
    def __calculateSlot(self, item):
        if item == None:
            return None
        elif item.category.name == "Drone":
            return Slot.DRONE
        elif "loPower" in item.effects:
            return Slot.LOW
        elif "medPower" in item.effects:
            return Slot.MED
        elif "hiPower" in item.effects:
            return Slot.HIGH
        else:
            raise ValueError("Passed item does not fit in a low, med, high or drone slot")
    
    @validates("ID", "itemID", "ammoID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "ammoID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
        
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self)
        for effect in self.charge.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self)