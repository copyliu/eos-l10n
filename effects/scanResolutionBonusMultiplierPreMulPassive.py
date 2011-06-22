# Used by:
# Modules named like: Targeting System Subcontroller II (3 of 3)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties = True, penaltyGroup="scanResolutionBonusMultiplierPreMulPassive")
