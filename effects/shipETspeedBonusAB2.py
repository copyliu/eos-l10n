#Variations of item: Armageddon (4 of 5) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusAB2") * level)