#Items from group: Cyber Engineering (3 of 21)
#Items from group: Rig Energy Grid (6 of 30)
#Item: Energy Emission Systems
from customEffects import boostModListBySkillReq
def energyEmmisionSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringEnergyEmmisionSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Energy Emission Systems",
                           self.item, extraMult = level)