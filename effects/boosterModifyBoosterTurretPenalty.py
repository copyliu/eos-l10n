#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Alchemist' YA (2 of 2)
#Implants named like: Low grade Edge (5 of 6)
#Skill: Nanite Control
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    attrs = ("boosterTurretFalloffPenalty", "boosterTurretOptimalRange", "boosterTurretTrackingPenalty")
    for attr in attrs:
        fit.boosters.filteredItemBoost(lambda booster: attr in booster.itemModifiedAttributes,
                                       attr, container.getModifiedItemAttr("boosterAttributeModifier") * level)
