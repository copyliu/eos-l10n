#Items from group: Sensor Booster Script (2 of 2) [Charge]
#Items from group: Sensor Dampener Script (2 of 2) [Charge]
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("maxTargetRangeBonus", module.getModifiedChargeAttr("maxTargetRangeBonusBonus"))