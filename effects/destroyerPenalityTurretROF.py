#Used by:
#Ships from group: Destroyer (4 of 4)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                     "speed", ship.getModifiedItemAttr("destroyerROFpenality"))
