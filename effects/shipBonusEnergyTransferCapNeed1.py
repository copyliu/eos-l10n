#Used by: Ship: Augoror
from customEffects import boostModListByReq
def shipBonusEnergyTransferCapNeed1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusAC",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item, extraMult = level)