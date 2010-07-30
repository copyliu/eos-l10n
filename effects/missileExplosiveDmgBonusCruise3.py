#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMU (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                       "explosiveDamage",container.getModifiedItemAttr("damageMultiplierBonus"))