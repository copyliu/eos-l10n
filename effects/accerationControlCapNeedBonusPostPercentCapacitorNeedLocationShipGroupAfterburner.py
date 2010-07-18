#Variations of item: Large Dynamic Fuel Valve I (2 of 2)
#Variations of item: Medium Dynamic Fuel Valve I (2 of 2)
#Variations of item: Small Dynamic Fuel Valve I (2 of 2)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))