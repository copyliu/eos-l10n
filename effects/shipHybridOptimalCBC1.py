#Used by:
#Ship: Ferox
#Ship: Vulture
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusBC1") * level)