#Used by: Item: Blue Pill Booster
from customEffects import boostModListByReq
def shieldBoostAmplifierPassiveLocationGroup(self, fitting):
    boostModListByReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                      lambda mod: mod.group.name == "Shield Booster", self.item)