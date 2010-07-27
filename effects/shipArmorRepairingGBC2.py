#Variations of item: Brutix (3 of 3) [Ship]
#Item: Myrmidon [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", ship.getModifiedItemAttr("shipBonusBC2") * level)