#Item: Biology [Skill]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' WA-2 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemIncrease(lambda: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)
