from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut
from model.effectHandlerHelpers import HandledItem

class Ship(ItemAttrShortcut, HandledItem):
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
        self.commandBonus = 0

    @property
    def item(self):
        return self.__item

    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes

    def clear(self):
        self.itemModifiedAttributes.clear()
        self.commandBonus = 0

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if forceProjected: return
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and effect.isType("passive"):
                 effect.handler(fit, self, ("ship",))
