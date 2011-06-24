# Used by:
# Modules named like: Memetic Algorithm Bank (6 of 6)
# Implant: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPX-1
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Hacking"),
                                  "accessDifficultyBonus",
                                  container.getModifiedItemAttr("accessDifficultyBonusModifier"))