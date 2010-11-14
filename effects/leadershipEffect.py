#Used by:
#Skill: Leadership
type = "gang"
gangBonus = "scanResolutionBonus"
gangBoost = "scanResolution"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("scanResolution", skill.getModifiedItemAttr("scanResolutionBonus") * skill.level)
