#Item: Afterburner [Skill]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-2 [Implant]
#Item: Zor's Custom Navigation Link [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Afterburner"),
                                     "duration", container.getModifiedItemAttr("durationBonus") * level)
