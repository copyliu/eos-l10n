#Item: Afterburner [Skill]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' EY-2 [Implant]
#Item: Zor's Custom Navigation Link [Implant]
type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Afterburner"),
                                     "duration", c.getModifiedItemAttr("durationBonus") * level)