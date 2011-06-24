# Used by:
# Ship: Skiff
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Exhumers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Deep Core Mining"),
                                  "damageCloudChance", ship.getModifiedItemAttr("eliteBonusBarge2") * level)
