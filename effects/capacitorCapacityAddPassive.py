#Items from group: Engineering Systems (16 of 16) [Subsystem]
#Item: Tengu Offensive - Magnetic Infusion Basin [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("capacitorCapacity",
                              module.getModifiedItemAttr("capacitorCapacity"))