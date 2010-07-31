#Used by:
#Skill: Multitasking
#Skill: Targeting
type = "passive"
def handler(fit, skill, context):
    fit.maxTargetsLocked += skill.getModifiedItemAttr("maxTargetBonus")
