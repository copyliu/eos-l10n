#Variations of item: Large Dynamic Fuel Valve I (2 of 2) [Module]
#Variations of item: Medium Dynamic Fuel Valve I (2 of 2) [Module]
#Variations of item: Small Dynamic Fuel Valve I (2 of 2) [Module]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))