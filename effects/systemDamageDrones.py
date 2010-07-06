#Used by: Item: Magnatar Effect Beacon
from customEffects import boostDroneListByReq, multiply
type = "projected"
def systemDamageDrones(self, fitting, state):
    boostDroneListByReq(fitting.modules, "damageMultiplier", "damageMultiplierMultiplier",
                      lambda drone: "damageMultiplier" in drone.attributes,
                      self.item, helper = multiply)