#Item: Guardian [Ship]
from customEffects import boostModListByReq
def eliteBonusLogisticEnergyTransferCapNeed1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Energy Transfer Array",
                      self.item, extraMult = level)
