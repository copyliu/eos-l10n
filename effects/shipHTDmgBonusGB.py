#Used by:
#Variations of ship: Dominix (3 of 3)
#Variations of ship: Megathron (4 of 5)
#Ship: Hyperion
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGB") * level)
