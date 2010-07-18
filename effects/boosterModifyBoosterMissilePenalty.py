#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Science Implants (2 of 7)
#Item: Low-grade Edge Alpha
#Item: Low-grade Edge Beta
#Item: Low-grade Edge Delta
#Item: Low-grade Edge Epsilon
#Item: Low-grade Edge Gamma
#Item: Nanite Control
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