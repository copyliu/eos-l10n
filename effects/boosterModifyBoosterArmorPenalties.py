type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorHPPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorHPPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorRepairAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorRepairAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)