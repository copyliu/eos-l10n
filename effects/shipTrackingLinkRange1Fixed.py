#Used by: Ship: Scimitar
from customEffects import boostModListByReq
def shipTrackingLinkRange1Fixed(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusMC",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)