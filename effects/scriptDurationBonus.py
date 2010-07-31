#Used by:
#Charge: Focused Warp Disruption
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("duration", module.getModifiedChargeAttr("durationBonus"))
    module.boostItemAttr("speedFactorBonus", module.getModifiedChargeAttr("speedFactorBonusBonus"))