#Item: Breacher
from customEffects import boostAmmoListBySkillReq
def shipMissileEMDamageMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusMF2",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)