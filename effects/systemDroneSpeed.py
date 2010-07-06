#Used by: Item: Magnatar Effect Beacon
from customEffects import boostDroneListByReq, multiply
type = "projected"
def systemDroneSpeed(self, fitting, state):
    boostDroneListByReq(fitting.modules, "maxVelocity", "maxDroneVelocityMultiplier",
                      lambda drone: True, self.item, helper = multiply)