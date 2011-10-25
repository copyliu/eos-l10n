# Used by:
# Modules from group: Magnetic Field Stabilizer (24 of 24)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                      "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                      stackingPenalties = True)