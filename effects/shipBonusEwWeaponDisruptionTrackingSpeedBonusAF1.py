#Item: Crucifier [Ship]
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionTrackingSpeedBonusAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "shipBonusAF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)