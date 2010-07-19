#Items from group: Cloaking Device (12 of 14) [Module]
#Item: Large Targeting System Subcontroller I [Module]
#Item: Medium Targeting System Subcontroller I [Module]
#Item: Small Targeting System Subcontroller I [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("scanResolution",
                              module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties = True)