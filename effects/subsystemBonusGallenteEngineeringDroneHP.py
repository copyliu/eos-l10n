#Used by: Item: Proteus Engineering - Augmented Capacitor Reservoir
from customEffects import boostDroneListByReq
def subsystemBonusGallenteEngineeringDroneHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Engineering Systems")
    boostDroneListByReq(fitting.drones, ("hp", "armorHP", "shieldCapacity"),
                        "subsystemBonusGallenteEngineering",
                        lambda drone: True, self.item, extraMult = level)