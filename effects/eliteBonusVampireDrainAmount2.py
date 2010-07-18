#Items from market group: Ships > Recon Ships > Amarr (2 of 2)
from customEffects import boostModListByReq
def eliteBonusVampireDrainAmount2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "powerTransferAmount", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)