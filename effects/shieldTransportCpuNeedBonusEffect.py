#Items from group: Logistics (2 of 4) [Ship]
from customEffects import boostModListByReq
def shieldTransportCpuNeedBonusEffect(self, fitting):
    boostModListByReq(fitting.modules, "cpu", "shieldTransportCpuNeedBonus",
                      lambda mod: mod.group.name == "Shield Transporter", self.item)