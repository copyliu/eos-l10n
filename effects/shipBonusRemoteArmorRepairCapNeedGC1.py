#Item: Exequror
from customEffects import boostModListByReq
def shipBonusRemoteArmorRepairCapNeedGC1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusGC",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)
