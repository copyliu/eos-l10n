type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda module: module.item.requiresSkill("Archaeology"),
                                     "accessDifficultyBonus",
                                     container.getModifiedItemAttr("accessDifficultyBonusModifier"))