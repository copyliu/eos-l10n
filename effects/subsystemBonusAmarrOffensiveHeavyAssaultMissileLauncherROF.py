#Item: Legion Offensive - Assault Optimization [Subsystem]
from customEffects import boostModListByReq
def subsystemBonusAmarrOffensiveHeavyAssaultMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusAmarrOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)