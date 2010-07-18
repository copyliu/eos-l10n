#Variations of item: Arbitrator (3 of 3) [Ship]
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionMaxRangeBonusAC1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "maxRangeBonus", "shipBonusAC",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "falloffBonus", "shipBonusAC",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)
