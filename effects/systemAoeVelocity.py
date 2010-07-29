#Items with name like: Magnetar Effect Beacon Class (6 of 6)
type = "projected
def handler(fit, beacon, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                  "aoeVelocity", beacon.getModifiedItemAttr("aoeVelocityMultiplier"))