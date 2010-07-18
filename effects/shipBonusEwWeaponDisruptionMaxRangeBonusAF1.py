#Item: Crucifier
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionMaxRangeBonusAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "maxRangeBonus", "shipBonusAF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "falloffBonus", "shipBonusAF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
