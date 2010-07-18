#Item: Augoror [Ship]
from customEffects import boostModListByReq
def energyTransferArrayMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "powerTransferRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item)