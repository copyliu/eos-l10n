#Used by: Ship: Flycatcher
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusDF1",
                       lambda skill: skill.name == "Rockets" or \
                       skill.name == "Standard Missiles",
                       self.item, extraMult = level)