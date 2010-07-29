#Items with name like: Projectile Ambit Extension (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "falloff", module.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties = True)