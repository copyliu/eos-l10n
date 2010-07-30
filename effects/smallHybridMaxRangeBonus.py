#Used by:
#Ship: Catalyst
#Ship: Cormorant
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", container.getModifiedItemAttr("maxRangeBonus"))
