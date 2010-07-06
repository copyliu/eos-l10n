#Used by: Item: Centurion Implant Set
from customEffects import boostModListByReq
def ewGroupRsdMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item)