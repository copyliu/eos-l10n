#Used by: Item: Harvest Implant Set
from customEffects import boostModListByReq
def stripMinerMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Strip Miner", self.item)