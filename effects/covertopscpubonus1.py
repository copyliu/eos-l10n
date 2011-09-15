# Used by:
# Ships from group: Covert Ops (4 of 4)
# Ships from group: Force Recon Ship (4 of 4)
# Ships from group: Stealth Bomber (4 of 4)
# Ships from group: Transport Ship (4 of 8)
# Subsystems named like: Offensive Covert Reconfiguration (4 of 4)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Cloaking Device",
                                     "cpu", container.getModifiedItemAttr("cloakingCpuNeedBonus"))