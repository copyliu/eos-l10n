# Used by:
# Modules from group: Stasis Web (19 of 19)
# Drone: Berserker SW-900
type = "active", "projected"
def handler(fit, module, context):
    if "projected" not in context:
        return
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"),
                           stackingPenalties = True)
