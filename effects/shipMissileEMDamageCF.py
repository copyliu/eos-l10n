#Item: Caldari Navy Hookbill [Ship]
#Item: Kestrel [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileEMDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusCF2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
