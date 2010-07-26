#Item: Multitasking [Skill]
#Item: Targeting [Skill]
def handler(fit, skill, context):
    fit.maxTargetsLocked += skill.getModifiedItemAttr("maxTargetBonus")