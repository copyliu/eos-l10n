#Item: Drone Navigation Computer I [Module]
from customEffects import boostDroneListByReq
import model.fitting
def droneMWDBoostOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostDroneListByReq(fitting.drones, "maxVelocity", "speedBoostFactor",
                            lambda drone: True, self.item)