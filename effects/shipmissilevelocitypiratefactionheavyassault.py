# Used by:
# Ship: Gila
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Assault Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusPirateFaction"))
