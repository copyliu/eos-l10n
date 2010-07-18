#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemEcmRadarStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "scanRadarStrengthBonus", "scanRadarStrengthMultiplier",
                      lambda mod: mod.group.name == "ECM",
                      self.item, helper = multiply)