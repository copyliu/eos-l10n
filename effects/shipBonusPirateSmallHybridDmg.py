#Item: Daredevil [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusPirateFaction"))