#Items from group: Exhumer (2 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Exhumers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                  "duration", ship.getModifiedItemAttr("eliteBonusBarge2") * level)