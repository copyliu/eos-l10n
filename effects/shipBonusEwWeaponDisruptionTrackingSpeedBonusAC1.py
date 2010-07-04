#Used by: Ship: Arbitrator
#               Pilgrim
#               Curse
from customEffects import boostModListByReq
def shipBonusEwWeaponDisruptionTrackingSpeedBonusAC1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "shipBonusAC",
                      lambda mod: mod.group.name == "Tracking Disruptor", self.item,
                      extraMult = level)