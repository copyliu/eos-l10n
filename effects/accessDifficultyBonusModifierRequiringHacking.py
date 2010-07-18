#Items from group: Rig Electronics (6 of 30) [Module]
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPX-1 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Hacking"),
                                  "accessDifficultyBonus",
                                  container.getModifiedItemAttr("accessDifficultyBonusModifier"))