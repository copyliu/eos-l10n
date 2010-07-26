#Items from group: Electronic Systems (4 of 16) [Subsystem]
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Scan Probe Launcher",
                                  "cpu", module.getModifiedItemAttr("cpuNeedBonus"))