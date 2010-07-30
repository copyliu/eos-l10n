#Items with name like: Exile Booster (3 of 4)
#Items with name like: Frentix Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", booster.getModifiedItemAttr("boosterTurretTrackingPenalty"))