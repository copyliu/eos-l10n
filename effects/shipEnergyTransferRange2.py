#Item: Basilisk [Ship]
from customEffects import boostModListByReq
def shipEnergyTransferRange2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "powerTransferRange", "shipBonusCC2",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item, extraMult = level)
