#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-2 [Implant]
#Item: Low-grade Edge Alpha [Implant]
#Item: Low-grade Edge Beta [Implant]
#Item: Low-grade Edge Delta [Implant]
#Item: Low-grade Edge Epsilon [Implant]
#Item: Low-grade Edge Gamma [Implant]
#Item: Nanite Control [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterAOEVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterAOEVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterMissileVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileExplosionCloudPenaltyFixed" in booster.itemModifiedAttributes,
                                   "boosterMissileExplosionCloudPenaltyFixed", container.getModifiedItemAttr("boosterAttributeModifier") * level)
