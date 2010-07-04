#Used by: Ship: Ashimmu
from customEffects import boostModListByReq
def shipEnergyVampireTransferAmountBonusAc(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "powerTransferAmount", "shipBonusAC",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)