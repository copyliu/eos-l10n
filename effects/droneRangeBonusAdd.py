#Items from group: Drone Control Range Module (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.droneControlRange += module.getModifiedItemAttr("droneRangeBonus")