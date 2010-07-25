#Item: Bhaalgorn [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Stasis Web",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusMB") * level)