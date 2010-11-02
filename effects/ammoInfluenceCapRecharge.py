#Used by:
#Charges from group: Advanced Artillery Ammo (6 of 6)
#Charges from group: Advanced Autocannon Ammo (6 of 6)
#Charges from group: Advanced Blaster Ammo (6 of 6)
#Charges from group: Advanced Railgun Ammo (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("rechargeRate", module.getModifiedChargeAttr("capacitorRechargeRateMultiplier") or 1)
