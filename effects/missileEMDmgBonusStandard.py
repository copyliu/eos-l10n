#Item: Hardwiring - Zainou 'Snapshot' ZMN1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN500 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))