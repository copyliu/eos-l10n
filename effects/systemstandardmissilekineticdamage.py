# Used by:
# Celestials named like: Wolf Rayet Effect Beacon Class (5 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "kineticDamage", beacon.getModifiedItemAttr("smallWeaponDamageMultiplier"))
