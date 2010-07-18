#Items from category: Ship (7 of 245)
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCF",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
