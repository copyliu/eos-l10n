#Item: Proteus Engineering - Augmented Capacitor Reservoir
from customEffects import boostDroneListByReq
def subsystemBonusGallenteEngineering2DroneMWD(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Engineering Systems")
    boostDroneListByReq(fitting.drones, "maxVelocity", "subsystemBonusGallenteEngineering2",
                        lambda drone: True, self.item, extraMult = level)