#Used by: Ship: Basilisk
from customEffects import boostModListByReq
def eliteBonusLogisticEnergyTransferCapNeed2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item, extraMult = level)