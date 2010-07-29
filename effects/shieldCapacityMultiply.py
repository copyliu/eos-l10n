#Items from group: Power Diagnostic System (31 of 31) [Module]
#Items from group: Reactor Control Unit (28 of 28) [Module]
#Items with name like: Flux (23 of 25)
#Items with name like: Power (74 of 103)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("shieldCapacity", module.getModifiedItemAttr("shieldCapacityMultiplier"))