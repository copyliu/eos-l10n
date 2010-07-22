#Variations of item: Large Hybrid Collision Accelerator I (2 of 2) [Module]
#Variations of item: Medium Hybrid Collision Accelerator I (2 of 2) [Module]
#Variations of item: Small Hybrid Collision Accelerator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Hybrid Weapon",
                                     "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties = True)