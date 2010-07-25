#Variations of item: Dominix (3 of 3) [Ship]
#Variations of item: Megathron (4 of 5) [Ship]
#Item: Hyperion [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGB") * level)