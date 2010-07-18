#Item: Bhaalgorn [Ship]
from customEffects import boostModListByReq
def shipEnergyNeutralizerTransferAmountBonusAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListByReq(fitting.modules, "energyDestabilizationAmount", "shipBonusAB",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)