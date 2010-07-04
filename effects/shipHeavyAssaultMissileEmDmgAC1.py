#Used by: Ship: Sacrilege
from customEffects import boostAmmoListBySkillReq
def shipHeavyAssaultMissileEmDmgAC1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusAC",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)