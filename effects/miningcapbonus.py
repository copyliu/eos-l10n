# Used by:
# Ship: Bantam
# Ship: Burst
# Ship: Navitas
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Mining Laser",
                                     "capacitorNeed", ship.getModifiedItemAttr("capacitorNeedMultiplier"))
