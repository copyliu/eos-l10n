#Used by: Ship: Kestrel
#               Caldari Navy Hookbill
from customEffects import boostAmmoListBySkillReq
def shipMissileExplosiveDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusCF2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
