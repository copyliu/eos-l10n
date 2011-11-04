# Used by:
# Charges named like: Fury Missile (12 of 12)
# Charges named like: Rage (12 of 12)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedChargeAttr("signatureRadiusBonus"))
