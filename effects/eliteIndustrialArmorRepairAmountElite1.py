#Items from group: Transport Ship (3 of 8) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", ship.getModifiedItemAttr("eliteBonusIndustrial1") * level)