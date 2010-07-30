#Item: Hardwiring - Zainou 'Snapshot' ZMT1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))