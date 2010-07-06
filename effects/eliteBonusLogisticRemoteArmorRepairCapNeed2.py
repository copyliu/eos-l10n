#Used by: Ship: Guardian
from customEffects import boostModListByReq
def eliteBonusLogisticRemoteArmorRepairCapNeed2(self, fitting):
    skill, level = fitting.getCharSkill("Logistics")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusLogistics2",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)