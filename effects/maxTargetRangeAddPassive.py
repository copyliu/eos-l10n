#Items from group: Electronic Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRange"))