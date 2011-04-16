#Used by:
#Implants from group: Booster (9 of 35)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "maxRange", booster.getModifiedItemAttr("boosterTurretOptimalRange"))