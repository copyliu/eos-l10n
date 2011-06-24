# Used by:
# Modules named like: Engine Thermal Shielding (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "duration", module.getModifiedItemAttr("durationBonus"))