#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMU (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
