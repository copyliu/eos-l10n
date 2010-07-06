#Used by: Item: Projectile Ambit Extension
#               Projectile Burst Aerator
#               Projectile Collision Accelerator
#               Projectile Discharge Elutration
#               Projectile Locus Coordinator
#               Projectile Metastasis Adjuster
from customEffects import boostModListByReq
def drawbackPowerNeedProjectiles(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Projectile Weapon", self.item)