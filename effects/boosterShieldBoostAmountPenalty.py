#Used by: Item: Crash Booster
#               Frentix Booster
#The standard mindflood booster also has this effect but it's bugged and uses another one
type = "boosterSideEffect"
from customEffects import boostModListByReq
def boosterShieldBoostAmountPenalty(self, fitting):
    boostModListByReq(fitting.modules, "shieldBonus", "boosterShieldBoostAmountPenalty",
                      lambda mod: mod.group.name == "Shield Booster", self.item)