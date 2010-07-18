#Item: Orca
from customEffects import boostModListByReq
def zColinOrcaTractorRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "shipOrcaTractorBeamRangeBonus1",
                      lambda mod: mod.group.name == "Tractor Beam", self.item)
    