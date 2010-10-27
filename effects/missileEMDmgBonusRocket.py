#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMR (3 of 3)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))
