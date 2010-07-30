#Item: Capital Hybrid Turret [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Hybrid Turret"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)