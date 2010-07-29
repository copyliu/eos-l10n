#Items with name like: Apocalypse (2 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                    "maxRange", ship.getModifiedItemAttr("shipBonusAB2") * level)