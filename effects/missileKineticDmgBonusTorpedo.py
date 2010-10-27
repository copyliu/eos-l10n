#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMT (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
