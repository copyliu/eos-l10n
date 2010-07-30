#Item: Paladin [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                    "speedFactor", ship.getModifiedItemAttr("shipBonusAB") * level)