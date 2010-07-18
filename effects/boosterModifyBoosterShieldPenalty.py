type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldCapacityPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldCapacityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "shieldBoostMultiplier" in booster.itemModifiedAttributes,
                                   "shieldBoostMultiplier", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldBoostAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldBoostAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)