# Used by:
# Modules from group: Gyrostabilizer (19 of 19)
# Modules named like: TEST Damage Mod (5 of 5)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                  stackingPenalties = True)