# Used by:
# Ship: Harbinger
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusBC2") * level)