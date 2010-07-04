#Used by: Skill: Cynosural Field Theory
#          Ship: Force Recons
from customEffects import boostModListBySkillReq
def cynosuralTheoryConsumptionBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "consumptionQuantity", "consumptionQuantityBonusPercentage",
                           lambda skill: skill.name == "Cynosural Field Theory",
                           self.item, extraMult = level)
