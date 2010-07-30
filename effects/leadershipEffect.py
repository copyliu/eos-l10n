#Item: Leadership [Skill]
type = "gang"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("scanResolution", skill.getModifiedItemAttr("scanResolutionBonus") * skill.level)