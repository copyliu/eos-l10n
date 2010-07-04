#Used by: Item: Proteus Defensive - Nanobot Injector
from customEffects import boostModListByReq
def subsystemBonusGallenteDefensiveArmorRepairAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Defensive Systems")
    boostModListByReq(fitting.modules, "armorDamageAmount", "subsystemBonusGallenteDefensive",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)