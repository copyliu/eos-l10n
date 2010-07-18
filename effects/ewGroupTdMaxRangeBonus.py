#Items from group: Cyberimplant (5 of 138) [Implant]
from customEffects import boostModListByReq
def ewGroupTdMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item)