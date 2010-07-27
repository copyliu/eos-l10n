#Item: Advanced Drone Interfacing [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Drone Control Unit",
                                     "maxGroupActive", skill.level)