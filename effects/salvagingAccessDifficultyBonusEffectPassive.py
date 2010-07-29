#Items with name like: Salvage Tackle (6 of 6)
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPY-1 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Salvaging"),
                                  "accessDifficultyBonus", container.getModifiedItemAttr("accessDifficultyBonus"))