#Items from group: Reinforced Bulkhead (12 of 12) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedItemAttr("maxVelocityBonus"),
                              stackingPenalties = True)