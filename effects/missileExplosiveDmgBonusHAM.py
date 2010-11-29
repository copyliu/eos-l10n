#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZME (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "explosiveDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
