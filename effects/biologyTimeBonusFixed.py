#Used by: Skill: Biology
#         Item : Hardwiring 'Alchemist' WA-X
from customEffects import boostBoosterListByReq
def biologyTimeBonusFixed(self, fitting, level = 1):
    boostBoosterListByReq(fitting.boosters, "boosterDuration", "durationBonus",
                          lambda booster: True, self.item, extraMult = level)