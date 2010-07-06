#Used by: Item: Centurion Implant Set
from customEffects import boostModListByReq
def ewGroupTdMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item)