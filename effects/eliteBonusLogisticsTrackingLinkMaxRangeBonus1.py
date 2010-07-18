#Item: Scimitar
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkMaxRangeBonus1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "maxRangeBonus", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)
