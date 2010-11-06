#Used by:
#Ship: Mackinaw
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                     "miningAmount", ship.getModifiedItemAttr("miningAmountMultiplier"))
