from model.types import Item
from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict

class Module(object):
    """An instance of this class represents a module together with its ammo and modified attributes"""
    def __init__(self):
        self.__item = None
        self.__ammo = None
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__ammoModifiedAttributes = ModifiedAttributeDict()
        
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        if type(item) != Item and item != None: raise ValueError("Expecting an item, got a " + str(type(item)))
        self.__item = item
        self.__itemModifiedAttributes.clear()
        self.__ammoModifiedAttributes.clear()
        
    @property
    def ammo(self):
        return self.__ammo
    
    @ammo.setter
    def ammo(self, ammo):
        if type(ammo) != Item and ammo != None: raise ValueError("Expecting an item, got a " + str(type(ammo)))
        if not self.isValidAmmo(ammo): raise ValueError("Ammo does not fit in that slot")
        self.__ammo = ammo
        self.__itemModifiedAttributes.clear()
        self.__ammoModifiedAttributes.clear()
    
    def getModifiedAmmoAttr(self, key):
        if key in self.__ammoModifiedAttributes:
            return self.__ammoModifiedAttributes[key]
    
    def getModifiedItemAttr(self, key):
        if key in self.__itemModifiedAttributes:
            return self.__itemModifiedAttributes[key]
    
    def isValidAmmo(self, ammo):
        #Check sizes, if ammo size > module volume it won't fit
        if ammo == None: return True
        chargeVolume = self.getModifiedAmmoAttr("volume")
        moduleCapacity = self.getModifiedItemAttr("capacity")
        if chargeVolume != None and moduleCapacity != None and chargeVolume > moduleCapacity: return False
        
        chargeSize = self.getModifiedItemAttr("chargeSize")
        if chargeSize != None:
            ammoSize = self.getModifiedAmmoAttr('chargeSize')
            if chargeSize != ammoSize: return False

        ammoGroup = ammo.groupID
        for i in range(5):
            chargeGroup = self.getModifiedItemAttr('chargeGroup' + str(i))
            if chargeGroup == None: continue
            if ammoGroup == chargeGroup: return True
            
        return False