#Item: Oneiros
from customEffects import boostModListByReq
def shipTrackingLinkRange2Group(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusGC2",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, extraMult = level)