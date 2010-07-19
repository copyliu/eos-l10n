#Item: Scorpion [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusCB3") * level)