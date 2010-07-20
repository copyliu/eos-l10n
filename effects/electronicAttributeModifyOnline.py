#Items from group: Automated Targeting System (6 of 6) [Module]
type = "active"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("maxLockedTargets", module.getModifiedItemAttr("maxLockedTargetsBonus"))