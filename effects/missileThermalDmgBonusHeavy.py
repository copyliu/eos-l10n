#Item: Hardwiring - Zainou 'Snapshot' ZMH1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))