#Items with name like: Missiles (5 of 7)
#Item: Rockets [Skill]
#Item: Torpedoes [Skill]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "explosiveDamage", container.getModifiedItemAttr("damageMultiplierBonus"))