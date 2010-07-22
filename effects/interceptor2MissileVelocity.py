#Item: Crow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Interceptors").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusInterceptor2") * level)