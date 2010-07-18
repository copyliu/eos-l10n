#Items from group: Advanced Artillery Ammo (6 of 6)
#Items from group: Advanced Autocannon Ammo (6 of 6)
#Items from group: Advanced Blaster Ammo (6 of 6)
#Items from group: Advanced Railgun Ammo (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("rechargeRate", module.getModifiedChargeAttr("capacitorRechargeRateMultiplier"))