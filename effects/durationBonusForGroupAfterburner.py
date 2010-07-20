#Variations of item: Large Engine Thermal Shielding I (2 of 2) [Module]
#Variations of item: Medium Engine Thermal Shielding I (2 of 2) [Module]
#Variations of item: Small Engine Thermal Shielding I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "duration", module.getModifiedItemAttr("durationBonus"))