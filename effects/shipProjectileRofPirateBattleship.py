#Item: Machariel [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusPirateFaction"))