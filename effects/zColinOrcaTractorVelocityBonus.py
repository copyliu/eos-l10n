#Used by: Ship: Orca
from customEffects import boostModListByReq
def zColinOrcaTractorVelocityBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxTractorVelocity", "shipOrcaTractorBeamVelocityBonus2",
                      lambda mod: mod.group.name == "Tractor Beam", self.item)
    