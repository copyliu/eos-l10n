# Used by:
# Modules from group: Drone Control Range Module (3 of 3)
type = "passive"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("droneRangeBonus")
    fit.extraAttributes.increase("droneControlRange", amount)
