type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Hacking"),
                                  "accessDifficultyBonus",
                                  container.getModifiedItemAttr("accessDifficultyBonusModifier"))