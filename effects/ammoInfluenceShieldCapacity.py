#Used by:
#Charges from group: Advanced Beam Laser Crystal (6 of 6)
#Charges from group: Advanced Railgun Ammo (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("shieldCapacity", module.getModifiedChargeAttr("shieldCapacityMultiplier"))