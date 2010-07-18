#Item: Hyperion
from customEffects import boostModListByReq
def shipBonusArmorRepairAmountGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListByReq(fitting.modules, "armorDamageAmount", "shipBonusGB2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)