#Used by: Ship: Scythe
from customEffects import boostModListByReq
def shipBonusTrackingLinkTrackingSpeedBonusMC1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "shipBonusMC",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)