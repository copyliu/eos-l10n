#Item: Drones [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.maxActiveDrons += skill.getModifiedItemAttr("maxActiveDroneBonus") * skill.level