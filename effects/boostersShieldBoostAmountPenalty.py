#FAIL
#Used by: Item: Mindflood Booster
type = "boosterSideEffect"
displayName = "Shield Booster Penalty"
from customEffects import boostModListByReq
def boostersShieldBoostAmountPenalty(self, fitting):
    boostModListByReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                      lambda mod: mod.group.name == "Shield Booster", self.item)