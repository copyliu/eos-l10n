#Used by: Item: Algid Energy Administrations Unit
#               Energy Ambit Extension
#               Energy Burst Aerator
#               Energy Collision Accelerator
#               Energy Discharge Elutration
#               Energy Locus Coordinator
#               Energy Metastasis Adjuster
from customEffects import boostModListByReq
def drawbackPowerNeedLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)