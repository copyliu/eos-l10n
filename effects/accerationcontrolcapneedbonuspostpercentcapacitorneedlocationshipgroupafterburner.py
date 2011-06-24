# Used by:
# Modules named like: Dynamic Fuel Valve (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))