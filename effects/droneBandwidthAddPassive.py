#Items from group: Engineering Systems (13 of 16) [Subsystem]
#Items from group: Offensive Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("droneBandwidth", module.getModifiedItemAttr("droneBandwidth"))