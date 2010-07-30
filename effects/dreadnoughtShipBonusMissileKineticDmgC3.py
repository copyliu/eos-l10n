#Item: Phoenix [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Dreadnought").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Citadel Cruise Missiles"),
                                    "kineticDamage", ship.getModifiedItemAttr("dreadnoughtShipBonusC3") * level)