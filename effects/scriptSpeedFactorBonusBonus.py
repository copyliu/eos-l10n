#Item: Focused Warp Disruption [Charge]
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("speedFactorBonus", module.getModifiedChargeAttr("speedFactorBonusBonus"))