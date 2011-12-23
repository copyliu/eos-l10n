# Used by:
# Modules from group: Heat Sink (25 of 25)
# Modules named like: TEST Damage Mod (5 of 5)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties = True)