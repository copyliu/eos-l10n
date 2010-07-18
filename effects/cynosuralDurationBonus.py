#Items from group: Force Recon Ship (4 of 4)
from customEffects import boostModListByReq
def cynosuralDurationBonus(self, fitting):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Cynosural Field", self.item)