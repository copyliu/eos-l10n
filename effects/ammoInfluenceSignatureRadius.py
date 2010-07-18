#Items from group: Advanced Beam Laser Crystal (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("signatureRadius", module.getModifiedChargeAttr("signatureRadiusMultiplier"))