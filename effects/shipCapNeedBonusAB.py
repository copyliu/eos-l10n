#Used by:
#Variations of ship: Apocalypse (3 of 4)
#Variations of ship: Armageddon (4 of 5)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                    "capacitorNeed", ship.getModifiedItemAttr("shipBonusAB") * level)