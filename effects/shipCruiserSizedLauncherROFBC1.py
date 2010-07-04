#Used by: Ship: Nighthawk
from customEffects import boostModListByReq
def shipCruiserSizedLauncherROFBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "speed", "shipBonusBC1",
                      lambda mod: mod.group.name == "Missile Launcher Assault" or \
                      mod.group.name == "Missile Launcher Heavy" or \
                      mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)