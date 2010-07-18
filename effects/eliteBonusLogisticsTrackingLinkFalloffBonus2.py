#Item: Oneiros
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkFalloffBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "falloffBonus", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)
