#Used by:
#Modules from group: Drone Control Range Module (2 of 2)
type = "passive"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("droneRangeBonus")
    fit.extraAttributes.increase("droneControlRange", amount)
