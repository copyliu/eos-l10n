#Variations of item: Celestis (3 of 3) [Ship]
from customEffects import boostModListByReq
def shipBonusEwRemoteSensorDampenerMaxTargetRangeBonusGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "maxTargetRangeBonus", "shipBonusGC2",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)
