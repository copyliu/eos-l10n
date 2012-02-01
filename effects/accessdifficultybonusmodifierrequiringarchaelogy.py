# Used by:
# Modules named like: Emission Scope Sharpener (6 of 6)
# Implant: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPW-1
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda module: module.item.requiresSkill("Archaeology"),
                                     "accessDifficultyBonus",
                                     container.getModifiedItemAttr("accessDifficultyBonusModifier"), position="post")
