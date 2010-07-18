#Items from group: Destroyer (4 of 4)
from customEffects import boostModListByReq, multiply
def destroyerPenalityTurretROF(self, fitting):
    boostModListByReq(fitting.modules, "speed", "destroyerROFpenality",
                      lambda mod: mod.group.name == "Hybrid Weapon" or \
                      mod.group.name == "Energy Weapon" or \
                      mod.group.name == "Projectile Weapon",
                      self.item, helper = multiply)
