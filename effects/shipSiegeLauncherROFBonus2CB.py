#Variations of item: Raven (3 of 4) [Ship]
#Item: Scorpion Navy Issue [Ship]
#Item: Widow [Ship]
from customEffects import boostModListByReq
def shipSiegeLauncherROFBonus2CB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "speed", "shipBonus2CB",
                      lambda mod: mod.group.name == "Missile Launcher Siege",
                      self.item, extraMult = level)
