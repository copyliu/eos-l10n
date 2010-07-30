#Item: Damnation [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusBC2") * level)