# Used by:
# Ship: Naga
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Missile Launcher Siege",
                                     "power", ship.getModifiedItemAttr("bcSiegeMissilePower"))
