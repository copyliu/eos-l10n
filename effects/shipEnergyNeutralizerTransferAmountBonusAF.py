#Used by: Ship: Sentinel
#               Cruor
from customEffects import boostModListByReq
def shipEnergyNeutralizerTransferAmountBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "energyDestabilizationAmount", "shipBonusAF",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)