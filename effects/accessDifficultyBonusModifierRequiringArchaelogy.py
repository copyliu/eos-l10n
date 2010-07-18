#Items from group: Rig Electronics (6 of 30) [Module]
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPW-1 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda module: module.item.requiresSkill("Archaeology"),
                                     "accessDifficultyBonus",
                                     container.getModifiedItemAttr("accessDifficultyBonusModifier"))