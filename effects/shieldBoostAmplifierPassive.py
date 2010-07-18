from customEffects import boostModListBySkillReq
def shieldBoostAmplifierPassive(self, fitting):
    boostModListBySkillReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                           lambda skill: skill.name == "Shield Operation",
                           self.item, useStackingPenalty = False)
