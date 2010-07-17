type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedChargeAttr("maxVelocityBonus"))