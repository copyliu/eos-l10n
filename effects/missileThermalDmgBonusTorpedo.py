#Item: Hardwiring - Zainou 'Snapshot' ZMT1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT500 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))