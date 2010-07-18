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
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldCapacityPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldCapacityPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "shieldBoostMultiplier" in booster.itemModifiedAttributes,
                                   "shieldBoostMultiplier", container.getModifiedItemAttr("boosterAttributeModifier") * level)
    fit.boosters.filteredItemBoost(lambda booster: "boosterShieldBoostAmountPenalty" in booster.itemModifiedAttributes,
                                   "boosterShieldBoostAmountPenalty", container.getModifiedItemAttr("boosterAttributeModifier") * level)