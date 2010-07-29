#Items with name like: Apocalypse (3 of 3)
#Variations of item: Armageddon (4 of 5) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                    "capacitorNeed", ship.getModifiedItemAttr("shipBonusAB") * level)