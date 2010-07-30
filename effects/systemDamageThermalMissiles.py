#Items with name like: Magnetar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.modules.filteredItemBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                  "thermalDamage", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))