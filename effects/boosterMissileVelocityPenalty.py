#Items from market group: Implants & Boosters > Booster (6 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", "boosterMissileVelocityPenalty")