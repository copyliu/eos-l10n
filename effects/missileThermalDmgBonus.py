#Items from group: Missile Launcher Operation (7 of 24) [Skill]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))