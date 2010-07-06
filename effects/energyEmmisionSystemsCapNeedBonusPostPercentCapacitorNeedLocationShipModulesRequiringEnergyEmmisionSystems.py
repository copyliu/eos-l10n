#Used by: Skill: Energy Emission Systems
#           Rig: Egress Port Maximizer
from customEffects import boostModListBySkillReq
def energyEmmisionSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringEnergyEmmisionSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Energy Emission Systems",
                           self.item, extraMult = level)