#Used by: Ship: Brutix
#               Eos
#               Astarte
#               Myrmidon
from customEffects import boostModListByReq
def shipArmorRepairingGBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "armorDamageAmount", "shipBonusBC2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)