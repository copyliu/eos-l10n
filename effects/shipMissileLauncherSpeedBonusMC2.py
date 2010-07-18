#Item: Scythe Fleet Issue
from customEffects import boostModListByReq
def shipMissileLauncherSpeedBonusMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "speed", "shipBonusMC2",
                      lambda mod: mod.group.name == "Missile Launcher Assault" or \
                      mod.group.name == "Missile Launcher Heavy" or \
                      mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)
