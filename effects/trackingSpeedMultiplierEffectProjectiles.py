#Items from group: Rig Projectile Weapon (6 of 30) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Projectile Weapon",
                                  "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"))