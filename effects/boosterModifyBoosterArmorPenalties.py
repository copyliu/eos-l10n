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
    level = container.level if context == "skill" else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorHPPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorHPPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterArmorRepairAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterArmorRepairAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)