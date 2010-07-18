#Item: Scimitar
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkTrackingSpeedBonus1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)