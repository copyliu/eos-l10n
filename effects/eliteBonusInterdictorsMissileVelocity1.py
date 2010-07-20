#Item: Heretic [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                  "maxVelocity", ship.getModifiedItemAttr("eliteBonusInterdictors1") * level)