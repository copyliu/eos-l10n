#Items with name like: Targeting System Subcontroller II (3 of 3)
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties = True)