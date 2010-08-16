#Used by:
#Skill: Advanced Drone Interfacing
type = "active"
def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Drone Control Unit",
                                     "maxGroupActive", skill.level)
