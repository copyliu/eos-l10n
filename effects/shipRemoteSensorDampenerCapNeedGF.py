#Item: Keres
from customEffects import boostModListByReq
def shipRemoteSensorDampenerCapNeedGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusGF",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)
