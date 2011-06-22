# Used by:
# Modules named like: Salvage Tackle (6 of 6)
# Implant: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPY-1
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Salvaging"),
                                  "accessDifficultyBonus", container.getModifiedItemAttr("accessDifficultyBonus"))