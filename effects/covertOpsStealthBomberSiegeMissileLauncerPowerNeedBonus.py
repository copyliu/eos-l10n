#Items from group: Stealth Bomber (4 of 4)
from customEffects import boostModListByReq, multiply
def covertOpsStealthBomberSiegeMissileLauncerPowerNeedBonus(self, fitting):
    boostModListByReq(fitting.modules, "power", "stealthBomberLauncherPower",
                      lambda mod: mod.group.name == "Missile Launcher Siege",
                      self.item, helper = multiply)