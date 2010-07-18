#Item: Blackbird
from customEffects import boostModListByReq
def shipBonusECMStrengthBonusCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules,
                      ("scanGravimetricStrengthBonus", "scanMagnetometricStrengthBonus",
                       "scanLadarStrengthBonus", "scanRadarStrengthBonus"),
                      "shipBonusCC", lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)