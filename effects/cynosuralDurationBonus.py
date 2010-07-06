#Used by: Ship: Falcon
#               Rapier
#               Arazu
#               Pilgrim
from customEffects import boostModListByReq
def cynosuralDurationBonus(self, fitting):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Cynosural Field", self.item)