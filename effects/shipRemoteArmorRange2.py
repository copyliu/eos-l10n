#Used by: Ship: Guardian
from customEffects import boostModListByReq
def shipRemoteArmorRange2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusAC2",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)