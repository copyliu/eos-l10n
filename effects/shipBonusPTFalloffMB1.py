#Item: Vargur [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                    "falloff", ship.getModifiedItemAttr("shipBonusMB") * level)