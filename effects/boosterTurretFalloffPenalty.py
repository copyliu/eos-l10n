#Items with name like: Drop Booster (3 of 4)
#Items with name like: X-Instinct Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "falloff", booster.getModifiedItemAttr("boosterTurretFalloffPenalty"))