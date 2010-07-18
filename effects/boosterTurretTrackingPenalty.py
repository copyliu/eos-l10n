type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", booster.getModifiedItemAttr("boosterTurretTrackingPenalty"))