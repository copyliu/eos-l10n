#Item: Sacrilege [Ship]
from customEffects import boostAmmoListBySkillReq
def shipHeavyAssaultMissileThermalDmgAC1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusAC",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)