#Item: Scorpion [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM Burst",
                                  "ecmBurstRange", ship.getModifiedItemAttr("shipBonusCB3") * level)