# Used by:
# Ship: Vangel
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Assault",
                                  "speed", ship.getModifiedItemAttr("shipBonusATC1"))
