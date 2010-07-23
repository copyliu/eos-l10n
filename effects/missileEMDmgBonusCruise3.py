#Item: Hardwiring - Zainou 'Snapshot' ZMU1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))