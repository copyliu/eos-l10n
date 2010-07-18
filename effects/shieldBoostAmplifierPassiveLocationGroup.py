#Items from group: Booster (5 of 34) [Implant]
from customEffects import boostModListByReq
def shieldBoostAmplifierPassiveLocationGroup(self, fitting):
    boostModListByReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                      lambda mod: mod.group.name == "Shield Booster", self.item)