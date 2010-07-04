#Used by: Ship: Guardian
#               Basilisk
from customEffects import boostModListByReq
def energyTransferPowerNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "power", "powerTransferPowerNeedBonus",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item)