#Items from group: Drone Tracking Modules (2 of 2) [Module]
from customEffects import multiply, boostDroneListByReq
import model.fitting
def droneTrackingComputerMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostDroneListByReq(fitting.drones, "trackingSpeed", "trackingSpeedMultiplier",
                            lambda drone: "trackingSpeed" in drone.attributes,
                            self.item, helper = multiply)
        boostDroneListByReq(fitting.drones, "maxRange", "maxRangeMultiplier",
                            lambda drone: "maxRange" in drone.attributes,
                            self.item, helper = multiply)