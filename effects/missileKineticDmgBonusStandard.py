#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMN (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                       "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))