# Used by:
# Variations of ship: Catalyst (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusDF1") * level)
