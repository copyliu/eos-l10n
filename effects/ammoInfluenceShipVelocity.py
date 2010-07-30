#Used by:
#Charges from group: Advanced Artillery Ammo (6 of 6)
#Charges from group: Advanced Autocannon Ammo (6 of 6)
#Charges from group: Advanced Railgun Ammo (6 of 6)
#Charges named like: Javelin (15 of 15)
#Charges named like: Precision Missile (12 of 12)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedChargeAttr("maxVelocityBonus"))