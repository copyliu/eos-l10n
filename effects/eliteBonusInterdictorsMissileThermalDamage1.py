#Used by:
#Ship: Eris
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Standard Missiles") or mod.item.requiresSkill("Rockets"),
                                  "thermalDamage", ship.getModifiedItemAttr("eliteBonusInterdictors1") * level)