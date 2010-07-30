#Item: Dramiel [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusPirateFaction"))