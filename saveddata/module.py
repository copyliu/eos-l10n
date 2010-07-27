from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut, ChargeAttrShortcut
from sqlalchemy.orm import validates, reconstructor
from model.effectHandlerHelpers import HandledItem, HandledCharge
from itertools import chain

class State():
    OFFLINE = -1
    ONLINE = 0
    ACTIVE = 1
    OVERHEATED = 2
    
class Slot():
    LOW = 1
    MED = 2
    HIGH = 3
    RIG = 4
    SUBSYSTEM = 5
    
class Module(HandledItem, HandledCharge, ItemAttrShortcut, ChargeAttrShortcut):
    """An instance of this class represents a module together with its charge and modified attributes"""
    
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.itemID = item.ID if item != None else None
        self.__charge = None
        self.state = State.ONLINE
        self.build()
    
    @reconstructor
    def init(self):
        from model import db
        item = db.getItem(self.itemID)
        self.__item = item
        self.__slot = self.__calculateSlot(item)
        self.__charge = db.getItem(self.chargeID) if self.chargeID != None else None
        
        self.build()
    
    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.item.attributes
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
        if self.charge != None:
            self.__chargeModifiedAttributes.original = self.charge.attributes
    
    @property
    def maxRange(self):
        maxRange = self.item.getModifiedItemAttr("maxRange")
        if maxRange != None: return maxRange
        else:
            delay = self.item.getModifiedItemAttr("explosionDelay")
            speed = self.item.getModifiedItemAttr("maxVelocity")
            if delay != None and speed != None:
                return delay * speed
        
    @property
    def slot(self):
        return self.__slot
    
    
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
        effectSlotMap = {"rigSlot" : Slot.RIG,
                         "loPower" : Slot.LOW,
                         "medPower" : Slot.MED,
                         "hiPower" : Slot.HIGH,
                         "subSystem" : Slot.SUBSYSTEM}
        if item == None:
            return None
        for effectName, slot in effectSlotMap.iteritems():
            if effectName in item.effects:
                return slot

        raise ValueError("Passed item does not fit in any known slot")
    
    @validates("ID", "itemID", "ammoID", "state")
    def validator(self, key, val):                
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "state" : lambda val: isinstance(val, int) and val >= -1 and val <= 2 and
                                     (val < 1 or self.item.isType("active")) and (val < 2 or self.item.isType("overheat")),
               "ammoID" : lambda val: isinstance(val, int)}
               
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
    
    def clear(self):
        self.itemModifiedAttributes.clear()
        self.chargeModifiedAttributes.clear()
        
    def calculateModifiedAttributes(self, fit, runTime):
        #We will run the effect when two conditions are met:
        #1: It makes sense to run the effect
        #    The effect is either offline
        #    or the effect is passive and the module is in the online state (or higher)
        #    or the effect is active and the module is in the active state (or higher)
        #    or the effect is overheat and the module is in the overheated state (or higher)
        #2: the runtimes match
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and \
               (effect.isType("offline") or 
               (effect.isType("passive") and self.state >= State.ONLINE) or \
               (effect.isType("active") and self.state >= State.ACTIVE) or \
               (effect.isType("overheat") and self.state >= State.OVERHEATED)):
                effect.handler(fit, self, "module")
                
        if self.charge != None:
            for effect in self.charge.effects.itervalues():
                if effect.runTime == runTime:
                    effect.handler(fit, self, "moduleCharge")