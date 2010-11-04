#Used by:
#Charge: Focused Warp Disruption
type = "passive"
runTime = "early"
def handler(fit, module, context):
    module.boostItemAttr("massBonusPercentage", module.getModifiedChargeAttr("massBonusPercentageBonus"))
