#Used by: Item: Legion Defensive - Nanobot Injector
from customEffects import boostModListByReq
def subsystemBonusAmarrDefensiveArmorRepairAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    boostModListByReq(fitting.modules, "armorDamageAmount", "subsystemBonusAmarrDefensive",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)