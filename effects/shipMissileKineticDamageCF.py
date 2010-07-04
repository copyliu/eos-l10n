#Used by: Ship: Condor
#               Heron
#               Kestrel
#               Caldari Navy Hookbill
#               Crow
#               Buzzard
#               Hawk
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCF",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
