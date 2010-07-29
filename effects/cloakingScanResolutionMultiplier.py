#Items from group: Cloaking Device (12 of 14) [Module]
#Items with name like: Targeting System Subcontroller I (3 of 3)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("scanResolution",
                              module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties = True)