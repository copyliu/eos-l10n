#Item: Gas Cloud Harvesting [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Gas Cloud Harvester",
                                     "maxGroupActive", skill.level)