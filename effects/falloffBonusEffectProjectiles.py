#Items from group: Rig Projectile Weapon (6 of 30) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "falloff", module.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties = True)