#Used by: Ship: Scythe
from customEffects import boostModListByReq
def shipBonusTrackingLinkMaxRangeBonusMC1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "maxRangeBonus", "shipBonusMC",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)
