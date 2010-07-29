#Variations of item: Large Signal Focusing Kit I (2 of 2) [Module]
#Variations of item: Medium Signal Focusing Kit I (2 of 2) [Module]
#Variations of item: Small Signal Focusing Kit I (2 of 2) [Module]
#Item: Survey [Skill]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Electronics"),
                                  "duration", container.getModifiedItemAttr("scanspeedBonus") * level)
