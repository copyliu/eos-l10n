#Used by: Ship: Inquisitor
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusAF",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)