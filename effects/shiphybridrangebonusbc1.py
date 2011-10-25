# Used by:
# Ship: Naga
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusBC1") * level)
