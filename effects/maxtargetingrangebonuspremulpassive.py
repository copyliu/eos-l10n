# Used by:
# Modules named like: Ionic Field Projector (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeMultiplier"),
                              stackingPenalties = True, penaltyGroup="preMul")
