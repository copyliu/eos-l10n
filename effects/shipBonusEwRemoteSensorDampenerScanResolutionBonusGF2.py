#Variations of item: Maulus (2 of 2) [Ship]
from customEffects import boostModListByReq
def shipBonusEwRemoteSensorDampenerScanResolutionBonusGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListByReq(fitting.modules, "scanResolutionBonus", "shipBonusGF2",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)