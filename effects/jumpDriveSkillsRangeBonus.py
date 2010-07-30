#Item: Jump Drive Calibration [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("jumpDriveRange", skill.getModifiedItemAttr("jumpDriveRangeBonus") * skill.level)