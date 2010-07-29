#Items with name like: Signal Focusing Kit (6 of 6)
#Item: Survey [Skill]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Electronics"),
                                  "duration", container.getModifiedItemAttr("scanspeedBonus") * level)
