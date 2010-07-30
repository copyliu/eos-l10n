#Item: Multitasking [Skill]
#Item: Targeting [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.maxTargetsLocked += skill.getModifiedItemAttr("maxTargetBonus")
