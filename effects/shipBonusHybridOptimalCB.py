#Item: Rokh [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                    "maxRange", ship.getModifiedItemAttr("shipBonusCB") * level)