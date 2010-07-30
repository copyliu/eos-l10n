#Items with name like: Fury Missile (12 of 12)
#Items with name like: Rage (12 of 12)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedChargeAttr("signatureRadiusBonus"))