#Items from group: Advanced Artillery Ammo (6 of 6) [Charge]
#Items from group: Advanced Autocannon Ammo (6 of 6) [Charge]
#Items from group: Advanced Railgun Ammo (6 of 6) [Charge]
#Items with name like: Javelin (15 of 15)
#Items with name like: Precision Missile (12 of 12)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedChargeAttr("maxVelocityBonus"))