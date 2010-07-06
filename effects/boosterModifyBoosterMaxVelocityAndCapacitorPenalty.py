#Used by: Skill: Nanite Control
#         Item : Hardwiring - 'Alchemist' YA-X
#                Edge Implant Set
from customEffects import boostBoosterListByReq
def boosterModifyBoosterMaxVelocityAndCapacitorPenalty(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterCapacitorCapacityPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterCapacitorCapacityPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterMaxVelocityPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterMaxVelocityPenalty" in booster.attributes,
                          self.item, extraMult = level)