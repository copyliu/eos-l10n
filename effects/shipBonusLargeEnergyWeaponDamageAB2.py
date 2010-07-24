#Item: Abaddon [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusAB2") * level)