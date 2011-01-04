#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZME (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "emDamage", implant.getModifiedItemAttr("damageMultiplierBonus"))
