#Item: Biology [Skill]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-2 [Implant]
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemIncrease(lambda: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)