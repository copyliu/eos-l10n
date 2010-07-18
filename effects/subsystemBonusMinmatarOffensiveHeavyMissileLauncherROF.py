#Item: Loki Offensive - Hardpoint Efficiency Configuration [Subsystem]
from customEffects import boostModListByReq
def subsystemBonusMinmatarOffensiveHeavyMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusMinmatarOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Heavy",
                      self.item, extraMult = level)
