#Items from group: Cyber Armor (3 of 24)
#Item: Capital Repair Systems
from customEffects import boostModListByReq
def capitalRepairSystemsSkillDurationBonus(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)