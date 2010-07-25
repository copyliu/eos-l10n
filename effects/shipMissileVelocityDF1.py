#Item: Flycatcher [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets") or mod.charge.requiresSkill("Standard Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusDF1") * level)