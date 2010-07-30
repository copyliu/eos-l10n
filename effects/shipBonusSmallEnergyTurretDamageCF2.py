#Item: Succubus [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusCF2") * level)