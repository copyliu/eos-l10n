#Used by: Ship: Sentinel
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionMaxRangeBonusAF2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "maxRangeBonus", "shipBonus2AF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "falloffBonus", "shipBonus2AF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
