#Used by: Ship: Griffin
#               Kitsune
from customEffects import boostModListByReq
def shipECMScanStrengthBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListByReq(fitting.modules,
                      ("scanGravimetricStrengthBonus", "scanLadarStrengthBonus",
                       "scanRadarStrengthBonus", "scanMagnetometricStrengthBonus"),
                      "shipBonusCF", lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)