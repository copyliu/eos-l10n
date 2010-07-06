#Used by: Skill: Nanite Control
#         Item : Hardwiring - 'Alchemist' YA-X
#                Edge Implant Set
from customEffects import boostBoosterListByReq
def boosterModifyBoosterMissilePenalty(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterAOEVelocityPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterAOEVelocityPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterMissileVelocityPenalty", "boosterAttributeModifier",
                          lambda booster: "boosterMissileVelocityPenalty" in booster.attributes,
                          self.item, extraMult = level)
    boostBoosterListByReq(fitting.boosters, "boosterMissileExplosionCloudPenaltyFixed", "boosterAttributeModifier",
                          lambda booster: "boosterMissileExplosionCloudPenaltyFixed" in booster.attributes,
                          self.item, extraMult = level)