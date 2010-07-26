#Items from group: Remote Sensor Booster (8 of 8) [Module]
type= "projected", "active"
def handler(fit, module, context):
    if context != "projected" or fit.ship.getModifiedItemAttr("disallowAssistance") == 1:
        return
    
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties = True)
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties = True)