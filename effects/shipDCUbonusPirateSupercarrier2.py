#Used by:
#Ship: Revenant
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Drone Control Unit",
                                     "maxGroupActive", ship.getModifiedItemAttr("shipBonusPirateFaction2"))
