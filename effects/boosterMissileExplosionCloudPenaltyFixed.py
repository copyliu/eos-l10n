#Items with name like: Exile Booster (3 of 4)
#Items with name like: Mindflood Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeCloudSize", booster.getModifiedItemAttr("boosterMissileAOECloudPenalty"))