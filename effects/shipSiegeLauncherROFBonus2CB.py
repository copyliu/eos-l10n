#Used by: Ship: Scorpion Navy Issue
#               Raven
#               Raven Navy Issue
#               Raven State Issue
#               Widow
from customEffects import boostModListByReq
def shipSiegeLauncherROFBonus2CB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "speed", "shipBonus2CB",
                      lambda mod: mod.group.name == "Missile Launcher Siege",
                      self.item, extraMult = level)
