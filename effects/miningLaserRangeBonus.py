#Item: Low-grade Harvest Alpha [Implant]
#Item: Low-grade Harvest Beta [Implant]
#Item: Low-grade Harvest Delta [Implant]
#Item: Low-grade Harvest Epsilon [Implant]
#Item: Low-grade Harvest Gamma [Implant]
from customEffects import boostModListByReq
def miningLaserRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Mining Laser", self.item)