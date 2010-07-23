#Item: Hardwiring - Zainou 'Snapshot' ZMH1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))