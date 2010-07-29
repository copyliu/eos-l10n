#Items with name like: Memetic Algorithm Bank (6 of 6)
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPX-1 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Hacking"),
                                  "accessDifficultyBonus",
                                  container.getModifiedItemAttr("accessDifficultyBonusModifier"))