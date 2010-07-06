#Used by: Item: Algid Hybrid Administrations Unit
#               Hybrid Ambit Extension
#               Hybrid Burst Aerator
#               Hybrid Collision Accelerator
#               Hybrid Discharge Elutration
#               Hybrid Locus Coordinator
#               Hybrid Metastasis Adjuster
from customEffects import boostModListByReq
def drawbackPowerNeedHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)