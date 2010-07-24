#Items from group: Tracking Disruption Script (2 of 2) [Charge]
#Items from group: Tracking Script (2 of 2) [Charge]
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("maxRangeBonus", module.getModifiedChargeAttr("maxRangeBonusBonus"))
    module.boostItemAttr("falloffBonus", module.getModifiedChargeAttr("falloffBonus"))