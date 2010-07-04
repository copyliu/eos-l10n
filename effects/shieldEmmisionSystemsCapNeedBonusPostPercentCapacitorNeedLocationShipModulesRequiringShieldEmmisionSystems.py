#Used by: Skill: Shield Emission Systems
from customEffects import boostModListBySkillReq
def shieldEmmisionSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringShieldEmmisionSystems(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda skill: skill.name == "Shield Emission Systems",
                      self.item, extraMult = level)