#Items from market group: Ships > Recon Ships > Amarr (2 of 2)
from customEffects import boostModListByReq
def eliteReconBonusEnergyNeutAmount2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "energyDestabilizationAmount", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)