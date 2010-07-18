#Item: Cruor [Ship]
#Item: Sentinel [Ship]
from customEffects import boostModListByReq
def shipEnergyDrainAmountAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "powerTransferAmount", "shipBonusAF",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)