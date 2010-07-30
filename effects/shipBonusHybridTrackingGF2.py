#Item: Ares [Ship]
#Item: Federation Navy Comet [Ship]
#Item: Tristan [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                    "trackingSpeed", ship.getModifiedItemAttr("shipBonusGF2") * level)