#Item: Oneiros [Ship]
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkTrackingSpeedBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)