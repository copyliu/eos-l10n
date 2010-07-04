#Used by: Skill: Shield Compensation
#          Item: Core Defence Capacitor Safeguard
from customEffects import boostModListByReq, boostModListBySkillReq
def shieldOperationSkillBoostCapacitorNeedBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        boostModListByReq(fitting.modules, "capacitorNeed", "shieldBoostCapacitorBonus",
                          lambda mod: mod.group.name == "Shield Booster",
                          self.item, useStackingPenalty = False, extraMult = level)
    if self.item.group.category.name == "Module":
        boostModListBySkillReq(fitting.modules, "capacitorNeed", "shieldBoostCapacitorBonus",
                               lambda skill: skill.name == "Shield Operation",
                               self.item, useStackingPenalty = True)
