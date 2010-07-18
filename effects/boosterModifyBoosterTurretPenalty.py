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