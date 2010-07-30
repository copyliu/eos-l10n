#Items from group: Command Ship (8 of 8) [Ship]
#Items from market group: Ships > Capital Industrial Ships (2 of 2)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Gang Coordinator",
                                     "maxGroupActive", ship.getModifiedItemAttr("maxGangModules"))