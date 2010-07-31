#Used by:
#Skill: Drones
type = "passive"
def handler(fit, skill, context):
    fit.maxActiveDrons += skill.getModifiedItemAttr("maxActiveDroneBonus") * skill.level