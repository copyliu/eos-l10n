#Items from group: Force Recon Ship (4 of 4)
#Item: Cynosural Field Theory
from customEffects import boostModListBySkillReq
def cynosuralTheoryConsumptionBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "consumptionQuantity", "consumptionQuantityBonusPercentage",
                           lambda skill: skill.name == "Cynosural Field Theory",
                           self.item, extraMult = level)
