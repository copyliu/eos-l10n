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
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretOptimalRange" in booster.itemModifiedAttributes,
                                   "boosterTurretOptimalRange", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretFalloffPenalty" in booster.itemModifiedAttributes,
                                   "boosterTurretFalloffPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterTurretTrackingPenalty" in booster.itemModifiedAttributes,
                                   "boosterTurretTrackingPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)