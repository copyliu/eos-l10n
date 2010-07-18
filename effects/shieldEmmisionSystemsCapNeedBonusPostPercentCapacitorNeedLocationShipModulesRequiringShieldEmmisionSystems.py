#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Shield Implants (3 of 3)
#Item: Shield Emission Systems [Skill]
from customEffects import boostModListBySkillReq
def shieldEmmisionSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringShieldEmmisionSystems(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda skill: skill.name == "Shield Emission Systems",
                      self.item, extraMult = level)