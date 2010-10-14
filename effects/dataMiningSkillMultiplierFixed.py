#Used by:
#Skill: Archaeology
#Skill: Hacking
#Skill: Salvaging
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill(skill),
                                     "accessDifficultyBonus", skill.getModifiedItemAttr("accessDifficultyBonus") * skill.level)
