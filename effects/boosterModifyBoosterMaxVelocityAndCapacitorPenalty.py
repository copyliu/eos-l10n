type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterCapacitorCapacityPenalty" in booster.itemModifiedAttributes,
                                   "boosterCapacitorCapacityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterMaxVelocityPenalty" in booster.itemModifiedAttributes,
                                   "boosterMaxVelocityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)