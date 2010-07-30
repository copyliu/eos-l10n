#Items with name like: Low-grade Edge (5 of 6)
#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' YA-2 [Implant]
#Item: Nanite Control [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldCapacityPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldCapacityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "shieldBoostMultiplier" in booster.itemModifiedAttributes,
                                   "shieldBoostMultiplier", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldBoostAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldBoostAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
