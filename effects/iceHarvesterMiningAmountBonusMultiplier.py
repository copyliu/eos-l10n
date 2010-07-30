#Used by:
#Ship: Mackinaw
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                  "miningAmount", 100)