#Items from group: Rig Shield (54 of 54) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("drawback"))