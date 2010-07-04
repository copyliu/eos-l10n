#Used by: Ship: Oneiros
from customEffects import boostModListByReq
def eliteBonusLogisticsTrackingLinkMaxRangeBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "maxRangeBonus", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)
