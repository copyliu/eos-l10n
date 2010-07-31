#Item: Leadership [Skill]
type = "gang", "passive"
def handler(fit, skill, context):
    if "gang" in context:
        fit.ship.boostItemAttr("scanResolution", skill.getModifiedItemAttr("scanResolutionBonus") * skill.level)
    else:
        skill.commandBonus = skill.getModifiedItemAttr("scanResolutionBonus") * skill.level