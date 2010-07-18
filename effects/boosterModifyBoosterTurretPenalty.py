#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Science Implants (2 of 7)
#Item: Low-grade Edge Alpha [Implant]
#Item: Low-grade Edge Beta [Implant]
#Item: Low-grade Edge Delta [Implant]
#Item: Low-grade Edge Epsilon [Implant]
#Item: Low-grade Edge Gamma [Implant]
#Item: Nanite Control [Skill]
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