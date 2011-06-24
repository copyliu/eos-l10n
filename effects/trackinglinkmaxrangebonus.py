# Used by:
# Ship: Scythe
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Link",
                                  "maxRange", ship.getModifiedItemAttr("maxRangeBonus"))
