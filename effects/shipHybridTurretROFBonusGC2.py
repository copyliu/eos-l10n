#Item: Exequror Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusGC2") * level)