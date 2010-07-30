#Item: Hyperion [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                    "armorDamageAmount", ship.getModifiedItemAttr("shipBonusGB2") * level)