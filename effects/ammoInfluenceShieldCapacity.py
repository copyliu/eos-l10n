type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("shieldCapacity", module.getModifiedChargeAttr("shieldCapacityMultiplier"))