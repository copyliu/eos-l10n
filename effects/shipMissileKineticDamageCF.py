#Variations of item: Condor (2 of 3) [Ship]
#Variations of item: Heron (2 of 2) [Ship]
#Item: Caldari Navy Hookbill [Ship]
#Item: Hawk [Ship]
#Item: Kestrel [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCF",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
