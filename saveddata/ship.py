from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut

class Ship(ItemAttrShortcut):
    REQUIRED_ATTRIBUTES = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    
    def __init__(self, item):
        for requiredAttr in self.REQUIRED_ATTRIBUTES:
            if not requiredAttr in  item.attributes:
                raise ValueError("Passed item is not a ship")

        self.__item = item
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = item.attributes
        self.armorRepair, self.shieldRepair, self.hullRepair, self.extraCapRecharge = 0, 0, 0, 0
        
    @property
    def item(self):
        return self.__item
    
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    def clear(self):
        self.itemModifiedAttributes.clear()
        
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                    effect.handler(self, self.ship)