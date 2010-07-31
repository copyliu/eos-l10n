#Used by:
#Charge: Focused Warp Disruption
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("signatureRadiusBonus", module.getModifiedChargeAttr("signatureRadiusBonusBonus"))
