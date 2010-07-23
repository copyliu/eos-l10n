#Item: Improved Crash Booster [Implant]
#Item: Standard Crash Booster [Implant]
#Item: Strong Crash Booster [Implant]
#Item: Synth Crash Booster [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeCloudSize", implant.getModifiedItemAttr("aoeCloudSizeBonus"))