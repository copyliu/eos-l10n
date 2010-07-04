#Used by: Ship: Falcon
#               Rook
from customEffects import boostModListByReq
def eliteReconBonusLadarStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "scanLadarStrengthBonus", "eliteBonusReconShip2",
                          lambda mod: mod.group.name == "ECM",
                          self.item, extraMult = level)