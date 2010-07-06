#Used by: Skill: Nanite Control
#         Item : Hardwiring - 'Alchemist' YA-X
#                Edge Implant Set
from customEffects import boostBoosterListByReq
def boosterModifyBoosterTurretPenalty(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterTurretOptimalRange", "boosterAttributeModifier",
                          lambda booster: "boosterTurretOptimalRange" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterTurretFalloffPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterTurretFalloffPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterTurretTrackingPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterTurretTrackingPenalty" in booster.attributes,
                          self.item, extraMult = level)