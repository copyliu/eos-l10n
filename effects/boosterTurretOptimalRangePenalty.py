#Items from group: Booster (9 of 34) [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "maxRange", booster.getModifiedItemAttr("boosterTurretOptimalRange"))