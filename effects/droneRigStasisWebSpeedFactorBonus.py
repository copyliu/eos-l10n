#Used by: Item: Stasis Drone Augmentor Rigs
from customEffects import boostDroneListByReq
def droneRigStasisWebSpeedFactorBonus(self, fitting, state):
    boostDroneListByReq(fitting.drones, "speedFactor", "webSpeedFactorBonus",
                        lambda drone: drone.group.name == "Stasis Webifying Drone",
                        self.item)
