#Item: Scimitar
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkFalloffBonus1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "falloffBonus", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)
