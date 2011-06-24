# Used by:
# Modules from group: Rig Armor (54 of 54)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("drawback"),
                           stackingPenalties = True)