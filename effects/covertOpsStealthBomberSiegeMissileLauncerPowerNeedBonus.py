#Used by: Ship: All stealth bombers
from customEffects import boostModListByReq, multiply
def covertOpsStealthBomberSiegeMissileLauncerPowerNeedBonus(self, fitting):
    boostModListByReq(fitting.modules, "power", "stealthBomberLauncherPower",
                      lambda mod: mod.group.name == "Missile Launcher Siege",
                      self.item, helper = multiply)