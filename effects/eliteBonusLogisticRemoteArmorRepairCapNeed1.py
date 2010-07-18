#Item: Oneiros
from customEffects import boostModListByReq
def eliteBonusLogisticRemoteArmorRepairCapNeed1(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics1",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)