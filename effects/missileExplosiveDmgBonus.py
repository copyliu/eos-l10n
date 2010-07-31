#Used by:
#Skills named like: Missiles (5 of 7)
#Skill: Rockets
#Skill: Torpedoes
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "explosiveDamage", container.getModifiedItemAttr("damageMultiplierBonus"))