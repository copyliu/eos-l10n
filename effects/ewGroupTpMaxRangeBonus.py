#Used by: Item: Centurion Implant Set
from customEffects import boostModListByReq
def ewGroupTpMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item)