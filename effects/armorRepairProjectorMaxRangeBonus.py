#Used by:
#Ship: Exequror
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Projector",
                                  "maxRange", ship.getModifiedItemAttr("maxRangeBonus"))