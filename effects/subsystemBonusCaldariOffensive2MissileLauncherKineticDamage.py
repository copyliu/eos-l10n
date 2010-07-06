#Used by: Item: Tengu Offensive - Accelerated Ejection Bay
from customEffects import boostAmmoListBySkillReq
def subsystemBonusCaldariOffensive2MissileLauncherKineticDamage(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "subsystemBonusCaldariOffensive2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)