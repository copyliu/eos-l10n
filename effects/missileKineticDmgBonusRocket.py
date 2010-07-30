#Item: Hardwiring - Zainou 'Snapshot' ZMR1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Rockets"),
                                       "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))