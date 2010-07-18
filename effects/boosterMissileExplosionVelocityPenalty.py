#Item: Improved Blue Pill Booster [Implant]
#Item: Standard Blue Pill Booster [Implant]
#Item: Strong Blue Pill Booster [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeVelocity", booster.getModifiedItemAttr("boosterAOEVelocityPenalty"))