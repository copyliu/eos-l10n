#Item: Jump Fuel Conservation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("jumpDriveConsumptionAmount", skill.getModifiedItemAttr("consumptionQuantityBonusPercentage") * skill.level)