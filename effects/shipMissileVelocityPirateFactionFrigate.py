# Used by:
# Ship: Worm
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles") or mod.charge.requiresSkill("Rockets"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusPirateFaction"))
