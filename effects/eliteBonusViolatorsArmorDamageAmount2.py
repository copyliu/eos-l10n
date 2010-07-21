#Item: Kronos [Ship]
#Item: Paladin [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Marauders").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", ship.getModifiedItemAttr("eliteBonusViolators2") * level)