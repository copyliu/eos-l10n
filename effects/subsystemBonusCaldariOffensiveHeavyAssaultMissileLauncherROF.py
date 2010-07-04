#Used by: Item: Tengu Offensive - Accelerated Ejection Bay
#               Tengu Offensive - Rifling Launcher Pattern
#               Tengu Offensive - Covert Reconfiguration
from customEffects import boostModListByReq
def subsystemBonusCaldariOffensiveHeavyAssaultMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusCaldariOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)