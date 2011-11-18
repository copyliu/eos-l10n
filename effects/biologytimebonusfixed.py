# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Alchemist' WA (2 of 2)
# Skill: Biology
# Skill: Nanobiology
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda bst: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)
