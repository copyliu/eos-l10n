#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMH (3 of 3)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))