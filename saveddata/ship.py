from model.modifiedAttributeDict import ModifiedAttributeDict

class Ship(object):
    REQUIRED_ATTRIBUTES = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    
    def __init__(self, item):
        for requiredAttr in self.REQUIRED_ATTRIBUTES:
            if not requiredAttr in  item.attributes:
                raise ValueError("Passed item is not a ship")

        self.__item = item
        self.__modifiedAttributes = ModifiedAttributeDict()
        self.__modifiedAttributes.original = item.attributes
        self.armorRepair, self.shieldRepair, self.hullRepair, self.extraCapRecharge = 0, 0, 0, 0
        
    @property
    def item(self):
        return self.__item
    
    @property
    def modifiedAttributes(self):
        return self.__modifiedAttributes
    
    