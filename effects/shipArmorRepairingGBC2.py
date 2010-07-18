#Items from market group: Ships > Command Ships > Gallente (2 of 2)
#Item: Brutix
#Item: Myrmidon
from customEffects import boostModListByReq
def shipArmorRepairingGBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "armorDamageAmount", "shipBonusBC2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)