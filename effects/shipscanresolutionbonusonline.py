# Used by:
# Modules from group: Signal Amplifier (11 of 11)
# Module: TEST Damage Mod
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties = True)
