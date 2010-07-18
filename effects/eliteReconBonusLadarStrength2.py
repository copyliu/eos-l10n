#Items from market group: Ships > Recon Ships > Caldari (2 of 2)
from customEffects import boostModListByReq
def eliteReconBonusLadarStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "scanLadarStrengthBonus", "eliteBonusReconShip2",
                          lambda mod: mod.group.name == "ECM",
                          self.item, extraMult = level)