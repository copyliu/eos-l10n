#Items from group: Rig Projectile Weapon (30 of 30)
from customEffects import boostModListByReq
def drawbackPowerNeedProjectiles(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Projectile Weapon", self.item)