def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemBoost(lambda mod: mod.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)