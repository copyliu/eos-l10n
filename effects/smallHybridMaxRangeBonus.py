#Item: Catalyst [Ship]
#Item: Cormorant [Ship]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", container.getModifiedItemAttr("maxRangeBonus"))
