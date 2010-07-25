#Item: Guardian [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusAC2") * level)