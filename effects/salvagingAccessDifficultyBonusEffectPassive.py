#Variations of item: Large Salvage Tackle I (2 of 2) [Module]
#Variations of item: Medium Salvage Tackle I (2 of 2) [Module]
#Variations of item: Small Salvage Tackle I (2 of 2) [Module]
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPY-1 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Salvaging"),
                                  "accessDifficultyBonus", container.getModifiedItemAttr("accessDifficultyBonus"))