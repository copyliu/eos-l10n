#Item: Large Blaster Specialization [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Blaster Specialization"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)