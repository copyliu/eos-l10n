#Used by: Item: Magnetar Effect Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemEcmLadarStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "scanLadarStrengthBonus", "scanLadarStrengthMultiplier",
                      lambda mod: mod.group.name == "ECM",
                      self.item, helper = multiply)