# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Alchemist' XA (2 of 2)
# Skill: Neurotoxin Recovery
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    for i in xrange(5):
        attr = "boosterEffectChance{0}".format(i+1)
        fit.boosters.filteredItemBoost(lambda booster: attr in booster.itemModifiedAttributes,
                                       attr, container.getModifiedItemAttr("boosterChanceBonus") * level)
