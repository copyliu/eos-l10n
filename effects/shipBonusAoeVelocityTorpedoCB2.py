#Item: Golem [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Torpedoes"),
                                    "aoeVelocity", ship.getModifiedItemAttr("shipBonus2CB") * level)