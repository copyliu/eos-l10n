#Used by: Ship: Guardian
#               Oneiros
from customEffects import boostModListByReq
def remoteArmorPowerNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "power", "remoteArmorPowerNeedBonus",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item)