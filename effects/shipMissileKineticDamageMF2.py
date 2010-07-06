#Used by: Ship: Breacher
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusMF2",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)