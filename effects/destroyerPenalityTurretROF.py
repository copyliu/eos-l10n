#Items from group: Destroyer (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    groups = "Hybrid Weapon", "Energy Weapon", "Projectile Weapon"
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name in groups,
                                     "speed", ship.getModifiedItemAttr("destroyerROFpenality"))