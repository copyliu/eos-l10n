#Item: Gila [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusPirateFaction"))