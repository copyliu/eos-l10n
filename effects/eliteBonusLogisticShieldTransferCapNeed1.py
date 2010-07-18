#Item: Basilisk [Ship]
from customEffects import boostModListByReq
def eliteBonusLogisticShieldTransferCapNeed1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)