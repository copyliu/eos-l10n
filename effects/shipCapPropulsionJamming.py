#Used by:
#Ships from group: Interceptor (8 of 8)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Propulsion Jamming"),
                                    "capacitorNeed", ship.getModifiedItemAttr("eliteBonusInterceptorRole"))