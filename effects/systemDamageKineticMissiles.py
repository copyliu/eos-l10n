# Used by:
# Celestials named like: Magnetar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                  "kineticDamage", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))