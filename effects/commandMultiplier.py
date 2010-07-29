#Items with name like: Warfare Specialist (4 of 5)
#Item: Mining Director [Skill]
runTime = "early"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill(skill),
                                     "commandBonus", skill.level)