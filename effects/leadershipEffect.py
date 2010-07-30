#Used by:
#Skill: Leadership
type = "gang"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("scanResolution", skill.getModifiedItemAttr("scanResolutionBonus") * skill.level)