#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListByReq, multiply
type = "projected"
def systemTrackingLinkOptimal(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonusMultiplier",
                      lambda mod: mod.group.name == "Tracking Link",
                      self.item, helper = multiply)