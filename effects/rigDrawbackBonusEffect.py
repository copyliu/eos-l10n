#Items from group: Mechanic (9 of 32) [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill(skill),
                                  "drawback", skill.getModifiedItemAttr("rigDrawbackBonus") * skill.level)
    