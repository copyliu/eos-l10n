# Used by:
# Variations of ship: Cyclone (3 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", ship.getModifiedItemAttr("shipBonusBC1") * level)
