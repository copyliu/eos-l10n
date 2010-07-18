#Items from market group: Implants & Boosters > Booster (9 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", booster.getModifiedItemAttr("boosterArmorRepairAmountPenalty"))