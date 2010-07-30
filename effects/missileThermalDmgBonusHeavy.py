#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMH (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))