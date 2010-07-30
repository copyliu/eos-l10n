#Item: Onyx [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Interdictors").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Heavy Assault Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusHeavyInterdictors1") * level)