#Used by:
#Skill: Archaeology
#Skill: Hacking
#Skill: Salvaging
type = "passive"
def handler(fit, skill, context):
    # TODO: remove hardcoding if it's possible
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill(skill),
                                     "accessDifficultyBonus", 5 * skill.level)
