#Items from group: Force Recon Ship (4 of 4) [Ship]
#Item: Cynosural Field Theory [Skill]
from customEffects import boostModListBySkillReq
def cynosuralTheoryConsumptionBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "consumptionQuantity", "consumptionQuantityBonusPercentage",
                           lambda skill: skill.name == "Cynosural Field Theory",
                           self.item, extraMult = level)
