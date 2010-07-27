#Item: Oneiros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Link",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusGC2") * level)