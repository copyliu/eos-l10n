#Used by: Item: Legion Offensive - Assault Optimization
from customEffects import boostModListByReq
def subsystemBonusAmarrOffensiveAssaultMissileLauncherROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListByReq(fitting.modules, "speed", "subsystemBonusAmarrOffensive",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)