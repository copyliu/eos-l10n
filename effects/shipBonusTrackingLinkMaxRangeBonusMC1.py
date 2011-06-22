# Used by:
# Ship: Scythe
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Link",
                                  "maxRangeBonus", ship.getModifiedItemAttr("shipBonusMC") * level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Link",
                                  "falloffBonus", ship.getModifiedItemAttr("shipBonusMC") * level)
