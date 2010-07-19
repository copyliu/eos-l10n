#Item: Capital Projectile Turret [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Projectile Turret"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)