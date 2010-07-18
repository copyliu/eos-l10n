#Item: Breacher [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileExplosiveDamageMF1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusMF",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)