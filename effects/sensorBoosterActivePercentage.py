#Items from group: Sensor Booster (12 of 12) [Module]
type = "active"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRange"),
                           stackingPenalties = True)
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties = True)