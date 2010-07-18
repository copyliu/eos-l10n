#Item: Guardian
from customEffects import boostModListByReq
def shipEnergyTransferRange1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "powerTransferRange", "shipBonusAC",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item, extraMult = level)
