#Item: Flycatcher [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Standard Missiles"),
                                  "kineticDamage", ship.getModifiedItemAttr("eliteBonusInterdictors1") * level)