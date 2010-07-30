#Item: Focused Warp Disruption [Charge]
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("signatureRadiusBonus", module.getModifiedChargeAttr("signatureRadiusBonusBonus"))
