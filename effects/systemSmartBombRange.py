#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemSmartBombRange(self, fitting, state):
    boostModListByReq(fitting.modules, "empFieldRange", "empFieldRangeMultiplier",
                      lambda mod: mod.group.name == "Smart Bomb",
                      self.item, helper = multiply)