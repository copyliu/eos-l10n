type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("signatureRadius", module.getModifiedChargeAttr("signatureRadiusMultiplier"))