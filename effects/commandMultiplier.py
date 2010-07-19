#Items from group: Leadership (5 of 14) [Skill]
runTime = "early"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill(skill),
                                     "commandBonus", skill.level)