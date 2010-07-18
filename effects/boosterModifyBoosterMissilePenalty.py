type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterAOEVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterAOEVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterMissileVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMissileExplosionCloudPenaltyFixed" in booster.itemModifiedAttributes,
                                   "boosterMissileExplosionCloudPenaltyFixed", container.getModifiedItemAttr("boosterAttributeModifier") * level)