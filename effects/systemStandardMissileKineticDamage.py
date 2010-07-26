#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                  "kineticDamage", beacon.getModifiedItemAttr("smallWeaponDamageMultiplier"))