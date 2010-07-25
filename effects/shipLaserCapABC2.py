#Variations of item: Prophecy (2 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Weapon",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusBC2") * level)