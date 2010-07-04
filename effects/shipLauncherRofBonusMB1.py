#Used by: Ship: Typhoon
#               Typhoon Fleet Issue
from customEffects import boostModListByReq
def shipLauncherRofBonusMB1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListByReq(fitting.modules, "speed", "shipBonusMB",
                      lambda mod: mod.group.name == "Missile Launcher Siege" or mod.group.name == "Missile Launcher Cruise",
                      self.item, extraMult = level)
