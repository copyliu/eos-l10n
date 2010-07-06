#Used by: Ship: Scimitar
from customEffects import boostModListByReq
def eliteBonusLogisticShieldTransferCapNeed2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)