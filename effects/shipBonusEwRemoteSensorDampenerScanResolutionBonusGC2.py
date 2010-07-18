#Variations of item: Celestis (3 of 3)
from customEffects import boostModListByReq
def shipBonusEwRemoteSensorDampenerScanResolutionBonusGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "scanResolutionBonus", "shipBonusGC2",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)