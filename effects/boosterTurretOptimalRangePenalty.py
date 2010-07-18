#Items from market group: Implants & Boosters > Booster (9 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "maxRange", booster.getModifiedItemAttr("boosterTurretOptimalRange"))