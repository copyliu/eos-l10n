#Items from group: Electronic Systems (16 of 16) [Subsystem]
def handler(fit, module, context):
    fit.ship.increaseItemAttr("scanResolution", module.getModifiedItemAttr("scanResolution"))