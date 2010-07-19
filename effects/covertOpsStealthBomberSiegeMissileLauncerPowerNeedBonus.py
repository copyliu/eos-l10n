#Items from group: Stealth Bomber (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Missile Launcher Siege",
                                  "power", ship.getModifiedItemAttr("stealthBomberLauncherPower"))