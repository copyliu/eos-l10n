#Items from group: Gyrostabilizer (19 of 19) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                  stackingPenalties = True)