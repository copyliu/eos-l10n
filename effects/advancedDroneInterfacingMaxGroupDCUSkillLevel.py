type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Drone Control Unit",
                                     "maxGroupActive", skill.level)