#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemHeatDamage(self, fitting, state):
    boostModListByReq(fitting.modules, "heatDamage", "heatDamageMultiplier",
                      lambda mod: "heatDamage" in mod.attributes,
                      self.item, helper = multiply)