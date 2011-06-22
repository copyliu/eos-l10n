# Used by:
# Celestials named like: Black Hole Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", beacon.getModifiedItemAttr("missileVelocityMultiplier"))