#Item: Sacrilege [Ship]
from customEffects import boostAmmoListBySkillReq
def shipHeavyAssaultMissileExplosiveDmgAC1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusAC",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)