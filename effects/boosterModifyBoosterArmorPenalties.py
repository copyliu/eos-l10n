#Items with name like: Low-grade Edge (5 of 6)
#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-2 [Implant]
#Item: Nanite Control [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorHPPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorHPPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorRepairAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorRepairAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
