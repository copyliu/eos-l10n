#Variations of item: Large Stasis Drone Augmentor I (2 of 2)
#Variations of item: Medium Stasis Drone Augmentor I (2 of 2)
#Variations of item: Small Stasis Drone Augmentor I (2 of 2)
from customEffects import boostDroneListByReq
def droneRigStasisWebSpeedFactorBonus(self, fitting, state):
    boostDroneListByReq(fitting.drones, "speedFactor", "webSpeedFactorBonus",
                        lambda drone: drone.group.name == "Stasis Webifying Drone",
                        self.item)
