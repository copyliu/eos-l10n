#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListByReq, multiply
type = "projected"
def systemTrackingLinkTracking(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "trackingSpeedBonusMultiplier",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, helper = multiply)