#Used by: Ship: Scimitar
#               Basilisk
from customEffects import boostModListByReq
def shieldTransportCpuNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "cpu", "shieldTransportCpuNeedBonus",
                      lambda mod: mod.group.name == "Shield Transporter", self.item)