#Used by: Item: Tengu Offensive - Accelerated Ejection Bay
from customEffects import boostAmmoListBySkillReq
def subsystemBonusCaldariOffensive3HeavyMissileVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "subsystemBonusCaldariOffensive3",
                       lambda skill: skill.name == "Heavy Missiles",
                       self.item, extraMult = level)