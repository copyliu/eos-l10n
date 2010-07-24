#Item: Kronos [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Stasis Web",
                                    "speedFactor", ship.getModifiedItemAttr("shipBonusGB2") * level)