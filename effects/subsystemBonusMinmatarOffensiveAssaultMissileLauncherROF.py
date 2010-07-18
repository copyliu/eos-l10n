#Item: Loki Offensive - Hardpoint Efficiency Configuration
from customEffects import boostModListByReq
def subsystemBonusMinmatarOffensiveAssaultMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusMinmatarOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)
