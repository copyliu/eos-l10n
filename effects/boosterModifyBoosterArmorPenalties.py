#Used by: Skill: Nanite Control
#         Item : Hardwiring - 'Alchemist' YA-X
#                Edge Implant Set
from customEffects import boostBoosterListByReq
def boosterModifyBoosterArmorPenalties(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterArmorHPPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterArmorHPPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterArmorRepairAmountPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterArmorRepairAmountPenalty" in booster.attributes,
                          self.item, extraMult = level)