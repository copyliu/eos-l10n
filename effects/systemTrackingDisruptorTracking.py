#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListByReq, multiply
type = "projected"
def systemTrackingDisruptorTracking(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "trackingSpeedBonusMultiplier",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, helper = multiply)