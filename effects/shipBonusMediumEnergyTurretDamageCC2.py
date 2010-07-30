#Item: Phantasm [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusCC2") * level)