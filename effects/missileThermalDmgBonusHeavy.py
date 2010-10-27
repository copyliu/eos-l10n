#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMH (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
