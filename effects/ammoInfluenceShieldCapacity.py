#Items from group: Advanced Beam Laser Crystal (6 of 6) [Charge]
#Items from group: Advanced Railgun Ammo (6 of 6) [Charge]
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("shieldCapacity", module.getModifiedChargeAttr("shieldCapacityMultiplier"))