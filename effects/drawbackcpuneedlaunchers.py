# Used by:
# Modules from group: Rig Launcher (36 of 36)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                  "cpu", module.getModifiedItemAttr("drawback"))
