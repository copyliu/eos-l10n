#Used by: Ship: Cormorant
#               Catalyst
from customEffects import boostModListBySkillReq
def smallHybridMaxRangeBonus(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item)