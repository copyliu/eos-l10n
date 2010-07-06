#Used by: Ship: Bhaalgorn
from customEffects import boostModListByReq
def shipEnergyVampireTransferAmountBonusAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListByReq(fitting.modules, "powerTransferAmount", "shipBonusAB",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)