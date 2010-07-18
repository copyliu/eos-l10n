#Item: Caldari Navy Hookbill
#Item: Kestrel
from customEffects import boostAmmoListBySkillReq
def shipMissileEMDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusCF2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
