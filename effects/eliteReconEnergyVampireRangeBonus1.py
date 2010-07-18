#Item: Curse [Ship]
from customEffects import boostModListByReq
def eliteReconEnergyVampireRangeBonus1(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "powerTransferRange", "eliteBonusReconShip1",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)
