def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemIncrease(lambda: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)