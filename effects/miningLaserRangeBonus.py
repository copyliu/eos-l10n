#Items from group: Cyberimplant (5 of 138)
from customEffects import boostModListByReq
def miningLaserRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Mining Laser", self.item)