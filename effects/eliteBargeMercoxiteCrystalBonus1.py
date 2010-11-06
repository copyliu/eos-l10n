#Used by:
#Ship: Skiff
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Exhumers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Mercoxit Mining Crystal",
                                    "specialisationAsteroidYieldMultiplier", ship.getModifiedItemAttr("eliteBonusBarge1") * level)
