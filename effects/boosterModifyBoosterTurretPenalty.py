#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Alchemist' YA (2 of 2)
#Implants named like: Low grade Edge (5 of 6)
#Skill: Nanite Control
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretOptimalRange" in booster.itemModifiedAttributes,
                                   "boosterTurretOptimalRange", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretFalloffPenalty" in booster.itemModifiedAttributes,
                                   "boosterTurretFalloffPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretTrackingPenalty" in booster.itemModifiedAttributes,
                                   "boosterTurretTrackingPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
