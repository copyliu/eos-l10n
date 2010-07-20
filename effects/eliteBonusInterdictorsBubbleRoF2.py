#Items from group: Interdictor (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Interdictors").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Interdiction Sphere Launcher",
                                  "speed", ship.getModifiedItemAttr("eliteBonusInterdictors2") * level)