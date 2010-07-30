#Items from group: Shield Amplifier (88 of 88) [Module]
#Items from group: Shield Extender (37 of 37) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("shieldCapacity", module.getModifiedItemAttr("capacityBonus"))