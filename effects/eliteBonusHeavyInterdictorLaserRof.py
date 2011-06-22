# Used by:
# Ship: Devoter
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "speed", ship.getModifiedItemAttr("eliteBonusHeavyInterdictors1") * level)
