#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostModListByReq, multiply
type = "projected"
def systemTrackingLinkTracking(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "trackingSpeedBonusMultiplier",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, helper = multiply)