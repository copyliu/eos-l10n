#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMN (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))
