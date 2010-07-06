#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemSmartBombRange(self, fitting, state):
    boostModListByReq(fitting.modules, "empFieldRange", "empFieldRangeMultiplier",
                      lambda mod: mod.group.name == "Smart Bomb",
                      self.item, helper = multiply)