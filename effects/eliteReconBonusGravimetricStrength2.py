#Used by: Ship: Rook
#               Falcon
from customEffects import boostModListByReq
def eliteReconBonusGravimetricStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "scanGravimetricStrengthBonus", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)