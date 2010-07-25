#Item: Bhaalgorn [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Vampire",
                                  "powerTransferAmount", ship.getModifiedItemAttr("shipBonusAB") * level)