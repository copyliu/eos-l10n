#Items from market group: Implants & Boosters > Booster (4 of 32)
type = "passive"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", booster.getModifiedItemAttr("armorDamageAmountBonus"))