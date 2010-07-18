#Item: Scythe
from customEffects import boostModListByReq
def trackingLinkMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item)