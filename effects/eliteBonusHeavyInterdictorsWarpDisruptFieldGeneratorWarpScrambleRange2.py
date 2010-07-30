#Items from group: Heavy Interdictor (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Warp Disrupt Field Generator",
                                  "warpScrambleRange", ship.getModifiedItemAttr("eliteBonusHeavyInterdictors2") * level)