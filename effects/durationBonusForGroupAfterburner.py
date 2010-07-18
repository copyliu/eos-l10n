#Variations of item: Large Engine Thermal Shielding I (2 of 2)
#Variations of item: Medium Engine Thermal Shielding I (2 of 2)
#Variations of item: Small Engine Thermal Shielding I (2 of 2)
from customEffects import boostModListByReq
def durationBonusForGroupAfterburner(self, fitting, state):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Afterburner", self.item)