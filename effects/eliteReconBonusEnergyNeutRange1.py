#Used by: Ship: Pilgrim
#               Curse 
from customEffects import boostModListByReq
def eliteReconBonusEnergyNeutRange1(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "energyDestabilizationRange", "eliteBonusReconShip1",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)