#Item: Hardwiring - Zainou 'Snapshot' ZMR1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))