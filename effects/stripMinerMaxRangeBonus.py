#Items from group: Cyberimplant (5 of 138) [Implant]
from customEffects import boostModListByReq
def stripMinerMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Strip Miner", self.item)