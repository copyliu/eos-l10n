#Items from group: Propulsion Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("maxVelocity", module.getModifiedItemAttr("maxVelocity"))