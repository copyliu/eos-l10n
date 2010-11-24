#Used by:
#Charges named like: Javelin (12 of 15)
#Charges named like: Precision Missile (12 of 12)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedChargeAttr("maxVelocityBonus"))