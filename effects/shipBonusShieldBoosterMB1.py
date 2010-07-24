#Item: Maelstrom [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Shield Booster",
                                    "shieldBonus", ship.getModifiedItemAttr("shipBonusMB1") * level)