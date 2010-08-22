#Used by:
#Ships from group: Destroyer (4 of 4)
type = "passive"
def handler(fit, ship, context):
    groups = ("Hybrid Weapon", "Energy Weapon", "Projectile Weapon")
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name in groups ,
                                     "speed", ship.getModifiedItemAttr("destroyerROFpenality"))
