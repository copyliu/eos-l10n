#Used by:
#Ship: Maelstrom
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                    "shieldBonus", ship.getModifiedItemAttr("shipBonusMB1") * level)