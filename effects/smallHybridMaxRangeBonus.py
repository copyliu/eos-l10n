#Items from group: Destroyer (2 of 4)
from customEffects import boostModListBySkillReq
def smallHybridMaxRangeBonus(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item)