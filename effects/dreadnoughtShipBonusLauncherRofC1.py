#Item: Phoenix [Ship]
from customEffects import boostModListByReq
def dreadnoughtShipBonusLauncherRofC1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Dreadnought")
    boostModListByReq(fitting.modules, "speed", "dreadnoughtShipBonusC1",
                      lambda mod: mod.group.name == "Missile Launcher Citadel", 
                      self.item, extraMult = level)
