#Used by: Ship: Condor
#               Caldari Navy Hookbill
from customEffects import boostAmmoListBySkillReq
def shipMissileRocketVelocityBonusCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCF2",
                            lambda skill: skill.name == "Rockets",
                            self.item, extraMult = level)
