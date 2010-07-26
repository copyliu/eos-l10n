#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.modules.filteredItemBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                  "thermalDamage", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))