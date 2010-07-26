#Items from group: Remote Sensor Damper (9 of 9) [Module]
type= "projected", "active"
def handler(fit, module, context):
    if context != "projected" or fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") == 1:
        return
    
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties = True)
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties = True)