#Item: Exequror
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "maxRange", ship.getModifiedItemAttr("maxRangeBonus"))