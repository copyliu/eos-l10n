#Items from group: Logistics (2 of 4)
from customEffects import boostModListByReq
def remoteArmorPowerNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "power", "remoteArmorPowerNeedBonus",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item)