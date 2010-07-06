#Used by: Ship: Maulus
#               Keres
from customEffects import boostModListByReq
def shipBonusEwRemoteSensorDampenerMaxTargetRangeBonusGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListByReq(fitting.modules, "maxTargetRangeBonus", "shipBonusGF2",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)
