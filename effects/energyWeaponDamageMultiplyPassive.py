#Variations of item: Large Energy Collision Accelerator I (2 of 2) [Module]
#Variations of item: Medium Energy Collision Accelerator I (2 of 2) [Module]
#Variations of item: Small Energy Collision Accelerator I (2 of 2) [Module] 
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties = True)