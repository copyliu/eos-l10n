#Item: Harbinger [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Weapon",
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusBC2") * level)