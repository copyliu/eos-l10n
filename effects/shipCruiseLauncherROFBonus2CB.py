#Variations of item: Raven (3 of 4) [Ship]
#Variations of item: Scorpion (2 of 4) [Ship]
from customEffects import boostModListByReq
def shipCruiseLauncherROFBonus2CB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "speed", "shipBonus2CB",
                      lambda mod: mod.group.name == "Missile Launcher Cruise",
                      self.item, extraMult = level)
