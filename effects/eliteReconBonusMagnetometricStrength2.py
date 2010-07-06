#Used by: Ship: Falcon
#               Rook
from customEffects import boostModListByReq
def eliteReconBonusMagnetometricStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "scanMagnetometricStrengthBonus", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)