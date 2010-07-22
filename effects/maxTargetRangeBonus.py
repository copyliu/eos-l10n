#Items from group: Warp Core Stabilizer (8 of 8) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties = True)