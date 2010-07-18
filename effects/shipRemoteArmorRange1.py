#Item: Oneiros
from customEffects import boostModListByReq
def shipRemoteArmorRange1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusGC",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)