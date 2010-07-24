#Items from group: Missile Launcher Operation (6 of 24) [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill(skill),
                                  "speed", skill.getModifiedItemAttr("rofBonus") * skill.level)