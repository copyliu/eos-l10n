type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))