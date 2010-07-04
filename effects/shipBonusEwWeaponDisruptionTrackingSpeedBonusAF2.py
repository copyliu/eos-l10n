#Used by: Ship: Sentinel
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionTrackingSpeedBonusAF2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "shipBonus2AF",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)