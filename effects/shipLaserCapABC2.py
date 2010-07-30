#Used by:
#Variations of ship: Prophecy (2 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusBC2") * level)