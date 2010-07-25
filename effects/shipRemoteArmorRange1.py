#Item: Oneiros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusGC") * level)