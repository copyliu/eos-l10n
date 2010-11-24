#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMR (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets"),
                                    "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
