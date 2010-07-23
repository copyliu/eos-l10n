#Item: Large Targeting System Subcontroller II [Module]
#Item: Medium Targeting System Subcontroller II [Module]
#Item: Small Targeting System Subcontroller II [Module]
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties = True)