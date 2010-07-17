type = "passive"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", booster.getModifiedItemAttr("armorDamageAmountBonus"))