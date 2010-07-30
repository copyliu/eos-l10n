#Item: Hardwiring - Zainou 'Snapshot' ZME1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))