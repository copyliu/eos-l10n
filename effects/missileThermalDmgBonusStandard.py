#Item: Hardwiring - Zainou 'Snapshot' ZMN1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))