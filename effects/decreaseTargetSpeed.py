#Items from group: Stasis Web (19 of 19) [Module]
#Item: Berserker SW-900 [Drone]
type = "active", "projected"
def handler(fit, module, context):
    if "projected" not in context: return
    if fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") == 1: return
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"),
                           stackingPenalties = True)
