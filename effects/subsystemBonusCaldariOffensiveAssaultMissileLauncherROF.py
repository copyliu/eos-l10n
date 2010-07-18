#Variations of item: Tengu Offensive - Accelerated Ejection Bay (3 of 4)
from customEffects import boostModListByReq
def subsystemBonusCaldariOffensiveAssaultMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusCaldariOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)