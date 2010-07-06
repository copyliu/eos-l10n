#Used by: Item: Harvest Implant Set
from customEffects import boostModListByReq
def miningLaserRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Mining Laser", self.item)