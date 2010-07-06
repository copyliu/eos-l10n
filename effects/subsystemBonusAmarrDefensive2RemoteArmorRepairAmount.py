#Used by: Item: Legion Defensive - Adaptive Augmenter
from customEffects import boostModListByReq
def subsystemBonusAmarrDefensive2RemoteArmorRepairAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    boostModListByReq(fitting.modules, "armorDamageAmount", "subsystemBonusAmarrDefensive2",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)