#Item: Nightmare [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonus2CB") * level)