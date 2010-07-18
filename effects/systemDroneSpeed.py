#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostDroneListByReq, multiply
type = "projected"
def systemDroneSpeed(self, fitting, state):
    boostDroneListByReq(fitting.modules, "maxVelocity", "maxDroneVelocityMultiplier",
                      lambda drone: True, self.item, helper = multiply)