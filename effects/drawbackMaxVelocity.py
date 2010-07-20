#Items from group: Rig Armor (54 of 54) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("drawback"),
                           stackingPenalties = True)