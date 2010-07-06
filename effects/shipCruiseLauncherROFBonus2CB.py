#Used by: Ship: Scorpion Navy Issue
#               Raven
#               Raven Navy Issue
#               Raven State Issue
#               Widow
from customEffects import boostModListByReq
def shipCruiseLauncherROFBonus2CB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "speed", "shipBonus2CB",
                      lambda mod: mod.group.name == "Missile Launcher Cruise",
                      self.item, extraMult = level)
