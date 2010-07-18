#Items from market group: Ships > Recon Ships > Minmatar (2 of 2)
from customEffects import boostModListByReq
def eliteReconStasisWebBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)