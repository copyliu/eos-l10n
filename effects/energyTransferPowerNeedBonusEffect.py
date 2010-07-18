#Items from group: Logistics (2 of 4)
from customEffects import boostModListByReq
def energyTransferPowerNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "power", "powerTransferPowerNeedBonus",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item)