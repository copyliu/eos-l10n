#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Alchemist' YA (2 of 2)
#Implants named like: Low grade Edge (5 of 6)
#Skill: Nanite Control
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterAOEVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterAOEVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterMissileVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileExplosionCloudPenaltyFixed" in booster.itemModifiedAttributes,
                                   "boosterMissileExplosionCloudPenaltyFixed", container.getModifiedItemAttr("boosterAttributeModifier") * level)
