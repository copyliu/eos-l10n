#Used by: Item: Engine Thermal Shielding
from customEffects import boostModListByReq
def durationBonusForGroupAfterburner(self, fitting, state):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Afterburner", self.item)