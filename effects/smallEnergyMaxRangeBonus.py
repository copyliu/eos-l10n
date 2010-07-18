#Item: Coercer [Ship]
from customEffects import boostModListBySkillReq
def smallEnergyMaxRangeBonus(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item)