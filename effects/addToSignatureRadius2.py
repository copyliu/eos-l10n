#Items from group: Shield Extender (37 of 37) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadiusAdd"))