#Item: Blackbird [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusCC2") * level)