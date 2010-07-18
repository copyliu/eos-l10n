#Item: Caldari Navy Hookbill
#Item: Condor
from customEffects import boostAmmoListBySkillReq
def shipMissileLightVelocityBonusCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCF2",
                            lambda skill: skill.name == "Standard Missiles",
                            self.item, extraMult = level)
