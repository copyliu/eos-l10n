#Item: Biology [Skill]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-2 [Implant]
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.boosters.filteredItemIncrease(lambda: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)