#Item: Hardwiring - Zainou 'Snapshot' ZMU1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                       "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))