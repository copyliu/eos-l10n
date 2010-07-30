#Used by:
#Skills from group: Missile Launcher Operation (7 of 24)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))