#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected
def handler(fit, beacon, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                  "aoeVelocity", beacon.getModifiedItemAttr("aoeVelocityMultiplier"))