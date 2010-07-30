#Items with name like: Hardwiring - Zainou 'Sharpshooter' (3 of 3)
#Item: Citadel Torpedoes [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Citadel Torpedoes"),
                                    "explosiveDamage", container.getModifiedItemAttr("damageMultiplierBonus") * level)
