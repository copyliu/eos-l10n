#Used by: Skill: Nanite Control
#         Item : Hardwiring - 'Alchemist' YA-X
#                Edge Implant Set
from customEffects import boostBoosterListByReq
def boosterModifyBoosterShieldPenalty(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterShieldCapacityPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterShieldCapacityPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "shieldBoostMultiplier", "boosterAttributeModifier",
                          lambda booster: "shieldBoostMultiplier" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterShieldBoostAmountPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterShieldBoostAmountPenalty" in booster.attributes,
                          self.item, extraMult = level)