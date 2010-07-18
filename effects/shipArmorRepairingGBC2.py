#Variations of item: Brutix (3 of 3) [Ship]
#Item: Myrmidon [Ship]
from customEffects import boostModListByReq
def shipArmorRepairingGBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "armorDamageAmount", "shipBonusBC2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)