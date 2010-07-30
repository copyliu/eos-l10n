#Item: Hardwiring - Zainou 'Snapshot' ZME1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))