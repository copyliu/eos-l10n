#Items from group: Booster (6 of 34) [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeCloudSize", booster.getModifiedItemAttr("boosterMissileAOECloudPenalty"))