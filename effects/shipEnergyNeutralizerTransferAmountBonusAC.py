#Item: Ashimmu
from customEffects import boostModListByReq
def shipEnergyNeutralizerTransferAmountBonusAC(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "energyDestabilizationAmount", "shipBonusAC",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)