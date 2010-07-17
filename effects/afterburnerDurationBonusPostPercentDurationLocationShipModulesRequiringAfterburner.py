type = "passive"
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Afterburner"),
                                     "duration", c.getModifiedItemAttr("durationBonus") * level)