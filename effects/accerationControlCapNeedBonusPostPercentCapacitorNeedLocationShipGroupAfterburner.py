#Used by: Item: Dynamic Fuel Valve
from customEffects import boostModListByReq
def accerationControlCapNeedBonusPostPercentCapacitorNeedLocationShipGroupAfterburner(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Afterburner", self.item)