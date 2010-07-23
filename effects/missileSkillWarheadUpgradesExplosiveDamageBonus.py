#Item: Warhead Upgrades [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "explosiveDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)