#Items from group: Engineering Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("rechargeRate", module.getModifiedItemAttr("rechargeRate"))